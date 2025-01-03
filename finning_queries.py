#This file contains all data required to do the connection


URL_TOKEN = "https://finning-dev-qas-cf-us-east-a3b5vigd.authentication.us10.hana.ondemand.com/oauth/token"
CUSTOMER_KEY = "sb-4a38c7a4-7f8d-453f-9092-3cb04fb627aa!b113541|it-rt-finning-dev-qas-cf-us-east-a3b5vigd!b56186"
CUSTOMER_SECRET = "3b933654-2118-4f62-b852-80fb33bb9cb1$B5K1DrYUHvtxtG06cF9F2z9vy1B1zwtdH2pfmHmScNM="
SERVICE_END_POINT = "https://finning-dev-qas-cf-us-east-a3b5vigd.it-cpi019-rt.cfapps.us10-002.hana.ondemand.com/http/execute_query"


SENTIMENTS_QUERY = (
            'SELECT TOP 1000 '+
	        '"ZSURVRECO", "ZTYPEOFSU", "NLSStatus", "0SALES_OFF" AS "SALES_OFF", "0SALESORG" AS "SALESORG", "0PLANT" AS "PLANT", "0CUST_GRP1" AS "CUST_GRP1", '+
	        '"0CUSTOMER" AS "CUSTOMER", "0CALMONTH" AS "CALMONTH", "0BILL_NUM" AS "BILL_NUM", "ZNOTESTAN", "ZNOTESRES", "ZNOTESREP", "ZNOTESREF", "ZNOTESQUA", '+
	        '"ZNOTESPRE", "ZNOTESIIM", "ZNOTESIAC", "ZNOTESEAS", "ZNOTESDUR", "ZNOTESCOM", "ZNOTESAVA", "ZNOTESADI", "NOTESFILLED", "NOTESANALYSED", '+ 
	        '"FULLY_PREDICTED", "NOTESCONCAT" '+
            'FROM "_SYS_BIC"."ZBW_FINNING.ZBW_FINNING_MARK.SAC.NLS/ZCV_003_SENTIMENT" '+
            'WHERE "FULLY_PREDICTED"=FALSE'
			
        )

KEY_WORDS_QUERY = (
            'SELECT '+
	        '"ZSAN_NTYP", '+
	        '"ZSAN_RES", '+
	        '"ZSAN_LAB", '+
	        '"ZSAN_KEY"  '+
            'FROM "_SYS_BIC"."ZBW_FINNING.ZBW_FINNING_MARK.SAC.NLS/ZCV_SAC_SENT_STANDARDS"'
)

