from flask import Flask, request, abort
import requests
import json
from Project.Config import *
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as BS

app = Flask(__name__)

def GET_BTC_PRICE():
    data = requests.get("https://api.bitkub.com/api/market/ticker?sym=THB_BTC")
    # BTC_PRICE = data.text.split('BTC')[1].split('last_price":')[1].split(',"volume_24hours')[0]
    # return BTC_PRICE
    return data.json()
    
def GET_ETH_PRICE():
    data = requests.get("https://api.bitkub.com/api/market/ticker?sym=THB_ETH")
    # BTC_PRICE = data.text.split('BTC')[1].split('last_price":')[1].split(',"volume_24hours')[0]
    # return BTC_PRICE
    return data.json()

def GET_XRP_PRICE():
    data = requests.get("https://api.bitkub.com/api/market/ticker?sym=THB_XRP")
    # BTC_PRICE = data.text.split('BTC')[1].split('last_price":')[1].split(',"volume_24hours')[0]
    # return BTC_PRICE
    return data.json()

def GET_DOT_PRICE():
    data = requests.get("https://api.bitkub.com/api/market/ticker?sym=THB_DOT")
    # BTC_PRICE = data.text.split('BTC')[1].split('last_price":')[1].split(',"volume_24hours')[0]
    # return BTC_PRICE
    return data.json()

def GET_WEATHER():
    pass

def GET_BCH_PRICE():
    data = requests.get("https://api.bitkub.com/api/market/ticker?sym=THB_BCH")
    # BTC_PRICE = data.text.split('BTC')[1].split('last_price":')[1].split(',"volume_24hours')[0]
    # return BTC_PRICE
    return data.json()

def GET_DOGE_PRICE():
    data = requests.get("https://api.bitkub.com/api/market/ticker?sym=THB_DOGE")
    # BTC_PRICE = data.text.split('BTC')[1].split('last_price":')[1].split(',"volume_24hours')[0]
    # return BTC_PRICE
    return data.json()

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json

        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        print(message)

        if "btc" in message or "BTC" in message :
            Reply_messasge = 'Details of Bitcoin(right now) : {}'.format(GET_BTC_PRICE())
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "ETH" in message or "eth" in message :
            Reply_messasge = 'Details of Etherium(right now) : {}'.format(GET_ETH_PRICE())
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "XRP" in message or "xrp" in message :
            Reply_messasge = 'Details of Ripple(right now) : {}'.format(GET_XRP_PRICE())
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "DOT" in message or "dot" in message :
            Reply_messasge = 'Details of Polkadot(right now) : {}'.format(GET_DOT_PRICE())
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "BCH" in message or "bch" in message :
            Reply_messasge = 'Details of BitcoinCash(right now) : {}'.format(GET_BCH_PRICE())
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif "DOGE" in message or "doge" in message :
            Reply_messasge = 'Details of DogeCoin(right now) : {}'.format(GET_DOGE_PRICE())
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)

@app.route('/')
def hello():
    return 'hello Nine, Good to see U again',200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) 
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200