# finning_python
Python code for finning sentiment analysis 

Using **Python 3.8.5** which is the latest more stable



To install dependencies download **requirements.txt** file and run

  **pip install -r /path/to/requirements.txt**



In **finning_constants.py** you need to set value of **ACCEPTED_PERCENTAGE** if you want the values more acurated. By default it has a **50** (**ACCEPTED_PERCENTAGE = 50**) so all the similarity of words above of **50%** of similarity will be considered, otherwise they will be discarded and marked as **Desconocido**



**Logs:**

The application will save logs for **successfully** queries and also for **errors**.

File with **success** events will have extension **.log**

File with **errors** will have extension **.err**

In **finning_constants.py** you need to declare a **valid path** with **write permissions** to create the log files in variable **LOG_FOLDER**. 
