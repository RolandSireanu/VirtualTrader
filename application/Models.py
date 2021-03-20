from . import db 


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    money = db.Column(db.Float, nullable=False)
    
    coinsOwned = db.relationship("Coins", back_populates="userOwner", uselist=True, foreign_keys="[Coins.uid]")

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

    def __repr__(self):
        return f"Coins('{self.eth}')"

    
    


db.create_all()

# print(UserModel.query.all())

# u1 = UserModel(username="Roland", password="1234")
# u2 = UserModel(username="Alexandru", password="1234")

# db.session.add(u1);
# db.session.add(u2);
# db.session.commit();
