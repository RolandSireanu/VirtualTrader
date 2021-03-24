from . import db
from .Models import UserModel, Coins
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
    