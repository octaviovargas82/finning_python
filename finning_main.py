#This is the main file of the application

import json
import ast
import datetime
import finning_constants
import finning_queries
import finning_helper

info_string=[]
error_string=[]

key_words_response = finning_helper.session.post(finning_queries.SERVICE_END_POINT, data=finning_queries.KEY_WORDS_QUERY)
keywords_data = json.dumps(key_words_response.json())
keywords_dict = ast.literal_eval(keywords_data)
keywords = keywords_dict["ROOT"]["select_response"]["row"]

#generate dictionary of keywords to search
finning_helper.generateSentimentsDictionary(keywords)    

sentiments_response = finning_helper.session.post(finning_queries.SERVICE_END_POINT, data=finning_queries.SENTIMENTS_QUERY)
sentiments_report_data = json.dumps(sentiments_response.json())
sentiment_dict = ast.literal_eval(sentiments_report_data)
sentiments = sentiment_dict["ROOT"]["select_response"]["row"]

def main():
     #while SAP HANA query returns records
     while len(sentiments)>0:
          #validate each poll
          for poll in sentiments:
               if(poll["ZNOTESTAN"]):
                    classification = finning_helper.clasify_comment("ZNOTESTAN", poll["ZNOTESTAN"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESTAN"], classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                    
               if(poll["ZNOTESRES"]):
                    classification = finning_helper.clasify_comment("ZNOTESRES", poll["ZNOTESRES"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESRES"],  classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                    
               if(poll["ZNOTESREP"]):
                    classification = finning_helper.clasify_comment("ZNOTESREP", poll["ZNOTESREP"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESREP"], classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                    
               if(poll["ZNOTESREF"]):
                    classification = finning_helper.clasify_comment("ZNOTESREF", poll["ZNOTESREF"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESREF"], classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                    
               if(poll["ZNOTESQUA"]):
                    classification = finning_helper.clasify_comment("ZNOTESQUA", poll["ZNOTESQUA"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESQUA"],  classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                    
               if(poll["ZNOTESPRE"]):
                    classification = finning_helper.clasify_comment("ZNOTESPRE", poll["ZNOTESPRE"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESPRE"],  classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                    
               if(poll["ZNOTESIAC"]):
                    classification = finning_helper.clasify_comment("ZNOTESIAC", poll["ZNOTESIAC"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESIAC"],  classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                    
               if(poll["ZNOTESEAS"]):
                    classification = finning_helper.clasify_comment("ZNOTESEAS", poll["ZNOTESEAS"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESEAS"],  classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                    
               if(poll["ZNOTESDUR"]):
                    classification = finning_helper.clasify_comment("ZNOTESDUR", poll["ZNOTESDUR"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESDUR"],  classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                    
               if(poll["ZNOTESCOM"]):
                    classification = finning_helper.clasify_comment("ZNOTESCOM", poll["ZNOTESCOM"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESCOM"],  classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                    
               if(poll["ZNOTESAVA"]):
                    classification = finning_helper.clasify_comment("ZNOTESAVA", poll["ZNOTESAVA"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESAVA"],  classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                         
               if(poll["ZNOTESADI"]):
                    classification = finning_helper.clasify_comment("ZNOTESADI", poll["ZNOTESADI"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESADI"],  classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())
                    
               if(poll["ZNOTESIIM"]):
                    classification = finning_helper.clasify_comment("ZNOTESIIM", poll["ZNOTESIIM"])
                    if(len(classification)==0):
                         classification.append({"Type":finning_constants.DESCONOCIDO,"Label":finning_constants.DESCONOCIDO})
                    finning_helper.insert_data(poll["ZSURVRECO"], finning_constants.ZSAN_TYP_DICTIONARY["ZNOTESIIM"],  classification[0]['Type'], classification[0]['Label'])
                    if(len(finning_helper.get_error_log())>0):
                         error_string.append(finning_helper.get_error_log())
                    if(len(finning_helper.get_info_log())>0):
                         info_string.append(finning_helper.get_info_log())

          if(len(error_string)>0):
               str_err=""
               for err in error_string:
                    if(len(err)>0):
                         for in_err in err:
                              t = datetime.datetime.now()
                              str_err += f"{t}-{in_err}\n"

               my_error_logger = finning_helper.get_logger(LOG_NAME="finning_errors.logger")
               my_error_logger.error(str_err)

          if(len(info_string)>0):
               str_log=""
               for log in info_string:
                    if(len(log)>0):
                         for in_log in log:
                              t = datetime.datetime.now()
                              str_log += f"{t}-{in_log}\n"
                                   
               my_info_logger = finning_helper.get_logger(LOG_NAME="finning_logs.logger")
               my_info_logger.info(str(str_log))
     
          #Validate again if there are more records in SAP HANA to loop again
          sentiments_response = finning_helper.session.post(finning_queries.SERVICE_END_POINT, data=finning_queries.SENTIMENTS_QUERY)
          sentiments_report_data = json.dumps(sentiments_response.json())
          sentiment_dict = ast.literal_eval(sentiments_report_data)
          sentiments = sentiment_dict["ROOT"]["select_response"]["row"] #if len (sentiments) == 0 while loop will finish, that means no more SAP HANA records to validate
