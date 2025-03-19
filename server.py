import os
from finning_main import main, deleteUnknowns, heartBeat
from flask import Flask
from cfenv import AppEnv
 
app = Flask(__name__)
env = AppEnv()
 
port = int(os.environ.get('PORT', 3000))
<<<<<<< HEAD

@app.route('/hello')
def hello():
   return "Hello World!"

@app.route('/')
def root():
   main()
   return "Ended"

@app.route('/deleteUnknowns')
def _deleteUnknowns():
   deleteUnknowns()
   return "deleteUnknowns"

@app.route('/heartBeat')
def _heartBeat():
   heartBeat()
   return "heartBeat"

=======
 
@app.route('/hello')
def hello():
   return "Hello World!"
 
@app.route('/')
def root():
   main()
 
>>>>>>> f97871dea0fa5141baa27381456601c6106fb798
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
