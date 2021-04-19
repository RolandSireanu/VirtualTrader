import requests
import json 
import time
from . import rq
import ipdb
from . import Models
from . import db

class DataRangeReader:
    headers = {
        'x-rapidapi-key': "1057bfb784msh8fa5180c3b466bdp1802bcjsnf6263a56e4b1",
        'x-rapidapi-host': "coingecko.p.rapidapi.com"
        }

    def readPricesOverTimer(self, coin):
        response = self.__makeGetRequest(coin)
        return response;


    def __makeGetRequest(self, coin):
        startPoint = int(time.time()) - (3600*24*30)
        url = f"https://coingecko.p.rapidapi.com/coins/{coin}/market_chart/range"
        querystring = {"from":str(startPoint),"vs_currency":"usd","to":str(int(time.time()))}
        
        response = requests.request("GET", url, headers=DataRangeReader.headers, params=querystring)
        if(response.status_code == 200):
            ipdb.set_trace()
            print(f"Response : {response}")
            data = json.loads(response.text)
            listPrices = data["prices"]
            print(len(listPrices))
            startFindingFrom = listPrices[len(listPrices)-1][0]
            points = [int((startFindingFrom - (i*(3600*24*1000)))) for i in range(30)]
            
            timePoints = list();

            for index in range(len(points)):
                startInterval = points[29 - index] - (3600*1000*3)
                endInterval = points[29 - index] + (3600*1000*3)
                for listPricesIdx in range(len(listPrices)):
                    if listPrices[listPricesIdx][0] < endInterval and listPrices[listPricesIdx][0] > startInterval:                    
                        timePoints.append(listPrices[listPricesIdx]);
                        break;
            timePoints[len(timePoints)-1] = listPrices[len(listPrices)-1];

            
            print(timePoints)
            
        return {
            "prices" : timePoints
        }
