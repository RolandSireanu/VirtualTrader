from . import db 

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return "User : " + str(self.username) ;


db.create_all()

# print(UserModel.query.all())

# u1 = UserModel(username="Roland", password="1234")
# u2 = UserModel(username="Alexandru", password="1234")

# db.session.add(u1);
# db.session.add(u2);
# db.session.commit();
