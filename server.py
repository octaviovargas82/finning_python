import os
from finning_main import main
from flask import Flask
from cfenv import AppEnv
 
app = Flask(__name__)
env = AppEnv()
 
port = int(os.environ.get('PORT', 3000))
 
@app.route('/hello')
def hello():
   return "Hello World!"
 
@app.route('/')
def root():
   main()
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
