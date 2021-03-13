import requests
import json 

class CryptoReader:

    url = "https://coingecko.p.rapidapi.com/simple/price"
    headers = {
    'x-rapidapi-key': "1057bfb784msh8fa5180c3b466bdp1802bcjsnf6263a56e4b1",
    'x-rapidapi-host': "coingecko.p.rapidapi.com"
    }

    def readPrices(self):
        
        querystring = {"ids":"bitcoin,ethereum,cardano,ripple,monero","vs_currencies":"usd"}
        response = requests.request("GET", CryptoReader.url, headers=CryptoReader.headers, params=querystring)
        data = json.loads(response.text);

        return [(k,v["usd"]) for k,v in data.items()];


