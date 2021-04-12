from . import db
from .CryptoReader import CryptoReader
from .Models import UserModel, Coins, TransactionModel
from collections import OrderedDict
import ipdb
import pprint

textToAcronym = {
    "bitcoin":"btc",
    "cardano":"ada",
    "ethereum":"eth",
    "monero":"xmr",
    "ripple":"xrp"
};


def Transaction(coin, user, quantity, action, transactionId=-1, pricePaid=0):

    cr = CryptoReader();
    currentPrices = dict(cr.readPrices());
    price = currentPrices[coin]
    
    currentUser = UserModel.query.filter_by(username=user).first()
    if(action == "buy"):
        print("BUY ACTION")
        if((quantity * price) <= currentUser.money):
            newValue = getattr(currentUser.coinsOwned[0],textToAcronym[coin]) + quantity; 
            setattr(currentUser.coinsOwned[0],textToAcronym[coin], newValue);
            currentUser.money = currentUser.money - (quantity*price);
            transaction=TransactionModel(uid=currentUser.id, coinType=coin, amount=quantity, price=price, money=quantity*price);
            currentUser.myTractions.append(transaction);
            db.session.commit();
        else:
            print("Not enough money !")
    elif(action == "sell"):
        print("SELL ACTION ! ")
        #trns = TransactionModel.query.filter_by(uid=currentUser.id, coinType=coin, amount=quantity, money=pricePaid).first();
        trns = TransactionModel.query.filter_by(uid=currentUser.id, id=transactionId).delete();
        db.session.commit();
        # if(trns):
        #     db.session.delete(trns);
        #     db.session.commit();
        
        howManyCoinsIOwn = getattr(currentUser.coinsOwned[0], textToAcronym[coin]);
        if(quantity <= howManyCoinsIOwn):
            print("HowManyCoinsIOwn : " + str(howManyCoinsIOwn))
            setattr(currentUser.coinsOwned[0],textToAcronym[coin], howManyCoinsIOwn - quantity);
            currentUser.money = currentUser.money + (quantity * price)
            # transaction=TransactionModel(uid=currentUser.id, coinType=coin, amount=quantity, money=quantity*price);
            # currentUser.myTractions.append(transaction);
            db.session.commit();
        else:
            print("You don't own enough coins ! ")

    else:
        print("ERROR: Undefined action ! ");
    

def AddUserToDB(username, password):
    user = UserModel(username=username, password=password, money=100000.0);
    db.session.add(user)

    coinModel = Coins(uid=user.id)
    coinModel.userOwner.append(user);
    db.session.add(coinModel)
    db.session.commit();
    
def GetCryptoFromDB(username):
    currentUser = UserModel.query.filter_by(username=username).first()
    return currentUser.coinsOwned[0].getCoins()
    
def computeTotal(trans, nrOfCoins, priceList):
    
    returnData = {}
    priceDict = dict(priceList);

    for k in nrOfCoins.keys():
        money = 0;
        for t in trans:
            if(t.coinType == k):
                money = money + ((t.money * -1));
        returnData[k] = money + (priceDict[k]*nrOfCoins[k]);

    return returnData


def buildDictOfPackages(transactions, prices):
    result = dict(list())
    dictPrices = dict(prices)
    
    for t in transactions:
        element = (t.amount, round(t.money,2), round(t.amount * dictPrices[t.coinType],2), t.id);
        if(t.coinType in result):
            result[t.coinType].append(element);
        else:
            result[t.coinType] = [element];

    return result;

def buildAccountsDict(prices):
    startMoney = 100000;

    usrs = UserModel.query.all();
    result = dict();

    for usr in usrs:
        coinsValue = 0;
        result[usr.username]={};

        for p in prices:
            owned = getattr(usr.coinsOwned[0],textToAcronym[p[0]]);
            coinsValue = coinsValue + owned * p[1];
        result[usr.username]["totalAccountValue"] = coinsValue + usr.money;
        result[usr.username]["coinsValue"] = coinsValue;
        result[usr.username]["money"] = usr.money;
        result[usr.username]["profitPerCoin"] = {}
        

        transactions = buildDictOfPackages(usr.myTractions, prices);

        for coin, acronym in textToAcronym.items():
            paidMoneyOnCurrentCoin = sum([t[1] for t in transactions.get(coin,[])])
            owned = getattr(usr.coinsOwned[0],textToAcronym[coin]);
            dictPrices = dict(prices);
            
            
            result[usr.username]["profitPerCoin"][coin] = (paidMoneyOnCurrentCoin, dictPrices[coin]*owned)

            

    orderedResult = OrderedDict(sorted(result.items(), key=lambda x : x[1]["totalAccountValue"], reverse=True))
    pprint.pprint(orderedResult)
    return orderedResult;

        
    # result = {u.username:u.money - startMoney for u in usrs}
    
