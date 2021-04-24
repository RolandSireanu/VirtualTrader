from . import db 
from collections import namedtuple


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=True)
    money = db.Column(db.Float, nullable=False)
    
    coinsOwned = db.relationship("Coins", back_populates="userOwner", uselist=True, foreign_keys="[Coins.uid]")
    myTractions = db.relationship("TransactionModel", back_populates="userOwnerTransaction", uselist=True, foreign_keys="[TransactionModel.uid]");


    def __repr__(self):
        return f"User('{self.username}','{self.money}')";

class Coins(db.Model):
    id = db.Column(db.Integer, primary_key=True);
    uid = db.Column(db.Integer, db.ForeignKey("user_model.id"))
    btc = db.Column(db.Integer, default=0)
    eth = db.Column(db.Integer, default=0)
    ada = db.Column(db.Integer, default=0)
    xrp = db.Column(db.Integer, default=0)
    xmr = db.Column(db.Integer, default=0)

    userOwner = db.relationship("UserModel", back_populates="coinsOwned", uselist=True)

    def getCoins(self):
        coins = {
            "bitcoin": self.btc,
            "ethereum": self.eth,
            "cardano": self.ada,
            "ripple": self.xrp,
            "monero": self.xmr
        };
        
        return coins;

    def __repr__(self):
        return f"Coins('{self.eth}')"

    
class TransactionModel(db.Model):
    id = db.Column(db.Integer, primary_key=True);
    uid = db.Column(db.Integer, db.ForeignKey("user_model.id"));
    coinType = db.Column(db.String, default="");
    amount = db.Column(db.Integer, default=0);
    price = db.Column(db.Float, default=0.0);
    money = db.Column(db.Float, default=0.0);

    userOwnerTransaction = db.relationship("UserModel");    


class PricesModel(db.Model):
    id = db.Column(db.Integer, primary_key=True);
    bitcoin = db.Column(db.Float, default=0.0)
    ethereum = db.Column(db.Float, default=0.0)
    cardano = db.Column(db.Float, default=0.0)
    ripple = db.Column(db.Float, default=0.0)
    monero = db.Column(db.Float, default=0.0)

# db.create_all();
# print(UserModel.query.all())

# u1 = UserModel(username="Roland", password="1234")
# u2 = UserModel(username="Alexandru", password="1234")

# db.session.add(u1);
# db.session.add(u2);
# db.session.commit();
