import requests
import json 
import time

import ipdb

class CryptoReader:

    url = "https://coingecko.p.rapidapi.com"
    headers = {
    'x-rapidapi-key': "1057bfb784msh8fa5180c3b466bdp1802bcjsnf6263a56e4b1",
    'x-rapidapi-host': "coingecko.p.rapidapi.com"
    }
    coinsRequested = ["bitcoin","ethereum","cardano","ripple","monero"]

    def readPrices(self):
        endPoint = "/simple/price"
        querystring = {"ids":",".join(CryptoReader.coinsRequested),"vs_currencies":"usd"}
        data = self.__makeGetRequest(CryptoReader.url+endPoint, CryptoReader.headers, querystring);
        return [(k,v["usd"]) for k,v in data.items()];

    # def readStats(self):
    #     for c in CryptoReader.coinsRequested:

    #         endPoint = f"/coins/{c}/market_chart/range";
    #         startPoint = (int)time.time() - (3600*24*30);
    #         now = (int)time.time();
            

    #         querystring = {"from":str(startPoint),"vs_currency":"usd","to":str(now)}
    #         data = __makeGetRequest(CryptoReader.url+endPoint, CryptoReader.headers, querystring);

    #     pass

    def __makeGetRequest(self, url, headers, params):
        response = requests.request("GET", url, headers=headers, params=params)
        data = json.loads(response.text)
        return data;

# url = "https://coingecko.p.rapidapi.com/coins/bitcoin/market_chart/range"



# headers = {
#     'x-rapidapi-key': "1057bfb784msh8fa5180c3b466bdp1802bcjsnf6263a56e4b1",
#     'x-rapidapi-host': "coingecko.p.rapidapi.com"
#     }
