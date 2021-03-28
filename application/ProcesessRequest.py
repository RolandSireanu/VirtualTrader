from . import db
from .Models import UserModel, Coins, TransactionModel
import ipdb

textToAcronym = {
    "bitcoin":"btc",
    "cardano":"ada",
    "ethereum":"eth",
    "monero":"xmr",
    "ripple":"xrp"
};


def Transaction(coin, price, user, quantity, action):

    currentUser = UserModel.query.filter_by(username=user).first()
    print("Action : " + action)
    if(action == "buy"):
        if((quantity * price) <= currentUser.money):
            newValue = getattr(currentUser.coinsOwned[0],textToAcronym[coin]) + quantity; 
            setattr(currentUser.coinsOwned[0],textToAcronym[coin], newValue);
            currentUser.money = currentUser.money - (quantity*price);
            transaction=TransactionModel(uid=currentUser.id, coinType=coin, action=0, amount=quantity, money=quantity*price);
            currentUser.myTractions.append(transaction);
            db.session.commit();
        else:
            print("Not enough money !")
    elif(action == "sell"):
        print("Sell action ! ")
        howManyCoinsIOwn = getattr(currentUser.coinsOwned[0], textToAcronym[coin]);
        if(quantity <= howManyCoinsIOwn):
            print("HowManyCoinsIOwn : " + str(howManyCoinsIOwn))
            setattr(currentUser.coinsOwned[0],textToAcronym[coin], howManyCoinsIOwn - quantity);
            currentUser.money = currentUser.money + (quantity * price)
            transaction=TransactionModel(uid=currentUser.id, coinType=coin, action=1, amount=quantity, money=quantity*price);
            currentUser.myTractions.append(transaction);
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
                money = money + ((t.money * -1) if t.action == 0 else t.money);
        returnData[k] = money + (priceDict[k]*nrOfCoins[k]);
        
    return returnData
