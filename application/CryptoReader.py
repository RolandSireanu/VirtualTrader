import requests
import json 
import time
from . import rq
import ipdb
from . import Models
from . import db


@rq.job
def updatePricesDb():
    endPoint = "/simple/price"
    querystring = {"ids":",".join(CryptoReader.coinsRequested),"vs_currencies":"usd"}
    data = None;
    while(data == None):
        response = requests.request("GET", CryptoReader.url+endPoint, headers=CryptoReader.headers, params=querystring)
        data = json.loads(response.text)
        print("Reading prices ... ")
        time.sleep(0.1);

    # return [(k,v["usd"]) for k,v in data.items()];

    pricesModel = Models.PricesModel.query.first();
    for k,v in data.items():
        setattr(pricesModel,k,v["usd"]);

    db.session.commit();
    print("Update db !")

updatePricesDb.cron("* * * * *","updatePricesDb-crono");

class CryptoReader:

    url = "https://coingecko.p.rapidapi.com"
    headers = {
    'x-rapidapi-key': "1057bfb784msh8fa5180c3b466bdp1802bcjsnf6263a56e4b1",
    'x-rapidapi-host': "coingecko.p.rapidapi.com"
    }
    coinsRequested = ["bitcoin","ethereum","cardano","ripple","monero"]



    def readPrices(self):
        pricesModel = Models.PricesModel.query.first();
        
        return [(k,getattr(pricesModel, k)) for k in CryptoReader.coinsRequested];

    def __makeGetRequest(self, url, headers, params):
        response = requests.request("GET", url, headers=headers, params=params)
        data = json.loads(response.text)
        return data;

# url = "https://coingecko.p.rapidapi.com/coins/bitcoin/market_chart/range"



# headers = {
#     'x-rapidapi-key': "1057bfb784msh8fa5180c3b466bdp1802bcjsnf6263a56e4b1",
#     'x-rapidapi-host': "coingecko.p.rapidapi.com"
#     }
