# finning_python
Python code for finning sentiment analysis 

Using **Python 3.8.5** which is the latest more stable



To install dependencies download **requirements.txt** file and run

  **pip install -r /path/to/requirements.txt**



In **finning_constants.py** you need to set value of **ACCEPTED_PERCENTAGE** if you want the values more acurated. By default it has a **50** (**ACCEPTED_PERCENTAGE = 50**) so all the similarity of words above of **50%** of similarity will be considered, otherwise they will be discarded and marked as **Desconocido**



**Logs:**

For logging I'm using **flask** logging from **sap.cf_logging**. 

Accoding with this page

https://github.com/SAP/cf-python-logging-support/blob/master/README.rst

I can use it along normal python logs 
