import requests
import json 
import time
from . import rq
import ipdb
from . import Models
from . import db


@rq.job
def updatePricesDb():

    url = "https://coingecko.p.rapidapi.com"
    headers = {
    'x-rapidapi-key': "1057bfb784msh8fa5180c3b466bdp1802bcjsnf6263a56e4b1",
    'x-rapidapi-host': "coingecko.p.rapidapi.com"
    }

    endPoint = "/simple/price"
    querystring = {"ids":",".join(CryptoReader.coinsRequested),"vs_currencies":"usd"}
    data = None;
    while(data == None):
        response = requests.request("GET", url+endPoint, headers=headers, params=querystring)
        if response is not None :
            data = json.loads(response.text)
        else:
            print("Invalid response from server,  keep trying ... ")
        print("Reading prices ... ")
        time.sleep(0.1);

    # return [(k,v["usd"]) for k,v in data.items()];

    pricesModel = Models.PricesModel.query.first();
    if(pricesModel is None):
        #First run , empty table
        firstElement = Models.PricesModel(bitcoin=0.0, ethereum=0.0, cardano=0.0, ripple=0.0, monero=0.0);
        db.session.add(firstElement);
    else:
        for k,v in data.items():
            setattr(pricesModel,k,v["usd"]);

    db.session.commit();
    print("Update db !")

updatePricesDb.cron("* * * * *","updatePricesDb-crono");

class CryptoReader:


    coinsRequested = ["bitcoin","ethereum","cardano","ripple","monero"]



    def readPrices(self):
        pricesModel = Models.PricesModel.query.first();        
        return [(k,getattr(pricesModel, k)) for k in CryptoReader.coinsRequested];
