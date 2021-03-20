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


def Buy(coin, price, user, quantity):

    curentUser = UserModel.query.filter_by(username=user).first()

    if((quantity * price) <= curentUser.money):
        newValue = getattr(curentUser.coinsOwned[0],textToAcronym[coin]) + quantity; 
        setattr(curentUser.coinsOwned[0],textToAcronym[coin], newValue);
        curentUser.money = curentUser.money - (quantity*price);
        db.session.commit();
    else:
        print("Not enough money !")
    
    
    
def AddUserToDB(username, password):
    user = UserModel(username=username, password=password, money=100000.0);
    db.session.add(user)

    coinModel = Coins(uid=user.id)
    coinModel.userOwner.append(user);
    db.session.add(coinModel)
    db.session.commit();
    
