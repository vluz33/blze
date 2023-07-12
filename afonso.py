import requests
from flask import Flask

app=Flask(__name__)


link1 = 'https://blaze.com/api/roulette_games/current'


req1=requests.get(link1)
d1=req1.json()

if d1['color']==0:
    token ='6078935508:AAGfzFwISS11HHzF6HlJI5WwjdL_8ZiqYh4'
    chat_id = '-1001911037404'
    message='\U00002b1c'
    URL = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+message
    resposta = requests.get(URL)

@app.route('/')
def homepage():
  return d1


app.run(host='0.0.0.0')
