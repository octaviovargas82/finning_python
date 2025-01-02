#This file contains all the methods used in the application
import logging
import requests
from thefuzz import fuzz
import finning_constants
import finning_queries
import datetime


t = datetime.datetime.now()
finning_file_error = f"{finning_constants.LOG_FOLDER}finning_{str(t.year)}_{str(t.month)}_{str(t.day)}_{str(t.hour)}_{str(t.minute)}_{str(t.second)}.err"
finning_file_info = f"{finning_constants.LOG_FOLDER}finning_{str(t.year)}_{str(t.month)}_{str(t.day)}_{str(t.hour)}_{str(t.minute)}_{str(t.second)}.log"


info_string=[]
error_string=[]

def put_info_log(info):
    info_string.append(info)
    
    
def get_info_log():
    return info_string        
    
def put_error_log(error):
    error_string.append(error)

def get_error_log():
    return error_string


def get_logger_error(    
        LOG_FORMAT     = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        LOG_NAME       = '',
        LOG_FILE_ERROR = finning_file_error):

    log           = logging.getLogger(LOG_NAME)
    log_formatter = logging.Formatter(LOG_FORMAT)
    #log.setLevel(logging.ERROR)

    # comment this to suppress console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    log.addHandler(stream_handler)
    
    file_handler_error = logging.FileHandler(LOG_FILE_ERROR, mode='w')
    file_handler_error.setFormatter(log_formatter)
    file_handler_error.setLevel(logging.ERROR)
    log.addHandler(file_handler_error)

    log.setLevel(logging.INFO)

    return log

def get_logger_info(    
        LOG_FORMAT     = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        LOG_NAME       = '',
        LOG_FILE_INFO  = finning_file_info):

    log           = logging.getLogger(LOG_NAME)
    log_formatter = logging.Formatter(LOG_FORMAT)
    

    # comment this to suppress console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    log.addHandler(stream_handler)

    file_handler_info = logging.FileHandler(LOG_FILE_INFO, mode='w')
    file_handler_info.setFormatter(log_formatter)
    file_handler_info.setLevel(logging.INFO)
    log.addHandler(file_handler_info)
    

    log.setLevel(logging.INFO)

    return log

sentiments_dict = dict()

#Identify which Notes cateogries we are using to avoid use all of them, for performance
def generateSentimentsDictionary(keywords): 
      for keyword in keywords:
        if(keyword["ZSAN_NTYP"] in sentiments_dict):
            #Add only note values we are using to existing note category in dictionary, this is for grouping by comments under the same category and 
            # iterate only on those categoryes for performance
            sentimenL = sentiments_dict.get(keyword["ZSAN_NTYP"])
            sentimenL.append({"ZSAN_RES":keyword["ZSAN_RES"], "ZSAN_LAB":keyword["ZSAN_LAB"], "ZSAN_KEY":keyword["ZSAN_KEY"]})
            sentiments_dict.update({keyword["ZSAN_NTYP"]: sentimenL})
        else:
            #Add new note value to dictionary
            sentiments_dict[keyword["ZSAN_NTYP"]]= [{"ZSAN_RES":keyword["ZSAN_RES"], "ZSAN_LAB":keyword["ZSAN_LAB"], "ZSAN_KEY":keyword["ZSAN_KEY"]}]
       
    
#Validate if comment contains key word in which percentage of similarity 
#we are validating the besdt option with the highest percentage of similarity. 
#but we are also defining the similarity percentaje should be higher than 50% (can be specified here finning_constants.ACCEPTED_PERCENTAGE)
#otherwise that means the phrase is not similar at all with key letters
def get_classification(comment, sentiments_filtered):
    sorted_array = dict() 
    if (len(comment.strip())>0):
        for w in sentiments_filtered:
           percentage = fuzz.token_sort_ratio(comment, w["ZSAN_KEY"])
           w["percentage"]=percentage
           if("sentiment" in sorted_array):
                prevSentiment = sorted_array.get("sentiment")
                if(prevSentiment["percentage"]<w["percentage"] and w["percentage"]>finning_constants.ACCEPTED_PERCENTAGE):
                    sorted_array["sentiment"]=w
           else:
               if(w["percentage"]>finning_constants.ACCEPTED_PERCENTAGE):
                    sorted_array["sentiment"]= {"ZSAN_RES":w["ZSAN_RES"], "ZSAN_LAB":w["ZSAN_LAB"], "ZSAN_KEY":w["ZSAN_KEY"], "percentage":percentage}
    if(sorted_array):
        return sorted_array
           
    #If comment cannot be classified with the words you have in the database it will be marked as this to let you know you need to classify it
    return finning_constants.DESCONOCIDO     


def clasify_comment(type, comment):
    sentiments_found=[]
    if (len(comment.strip())==0):
        #If comment is empty
        return finning_constants.SIN_COMENTARIOS
    else:
        senti = finning_constants.ZSAN_TYP_DICTIONARY[type]
        sentiments_poll = sentiments_dict.get(senti)
        if(sentiments_poll):
            sentiment_classification = get_classification(comment, sentiments_poll)
            if(sentiment_classification != finning_constants.DESCONOCIDO):
                if(sentiment_classification["sentiment"]["ZSAN_RES"] == finning_constants.POSITIVO 
                   or sentiment_classification["sentiment"]["ZSAN_RES"] == finning_constants.NEGATIVO):
                     sentiments_found.append({"Type":sentiment_classification["sentiment"]["ZSAN_RES"], "Label":sentiment_classification["sentiment"]["ZSAN_LAB"]})
    return sentiments_found       

def insert_data(pollId, note_type, sentiment, comments):
    
    if(len(pollId.strip())!=0 and len(note_type.strip())!=0 and len(sentiment)!=0 and len(sentiment.strip())!=0 and len(comments.strip())!=0):
        insert_query='UPSERT "SAPDB1"."TB_MKT_SAN_RES" VALUES (\''+pollId.strip()+'\',\''+note_type.strip()+'\',\''+sentiment.strip().upper()+'\',\''+comments.strip()+'\') WITH PRIMARY KEY;'
        response = session.post(finning_queries.SERVICE_END_POINT, data=insert_query)
        rj= response.json()["success"]
        if(rj):
          put_info_log(f'Sucessfully saved: {insert_query}') 
        else:  
          put_error_log(f'There was an error while trying to save the data {insert_query}:{response.json()["details"]}')

 
def get_access_token(url, client_id, client_secret):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    return response.json()["access_token"]



token = get_access_token(finning_queries.URL_TOKEN, finning_queries.CUSTOMER_KEY, finning_queries.CUSTOMER_SECRET)


headers = {
    'Content-Type': 'text/plain; charset=utf-8',
    'Authorization': 'Bearer '+str(token)
}

#creating a session and passing the token there
session = requests.Session()
session.headers.update(headers)

