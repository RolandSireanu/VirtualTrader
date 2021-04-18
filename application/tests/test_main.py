import os
import unittest
import json

from application import app
from application import db
from application import Models


TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resources/test.db'
        # os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        
        db.drop_all()
        db.create_all()
        prices = Models.PricesModel(bitcoin=1, ethereum=2, cardano=3, ripple=4, monero=5);
        db.session.add(prices);
        db.session.commit();
        

    def login(self, usr, pswd):
        return self.app.post(
        '/login',
        data=dict(usr=usr, pswd=pswd),
        follow_redirects=True
        )

    def register(self, usr, pswd, secondPswd):
        return self.app.post(
        '/register',
        data=dict(username=usr, pswd=pswd, secondPswd=secondPswd),
        follow_redirects=True
        )

    def test_register_login(self):
        ''' Test register and login '''
        
        registerResponse = self.register("Roland","226268", "226268");
        loginResponse = self.login("Roland", "226268");
        self.assertEqual(loginResponse.status_code, 200)
        response = self.app.get("/dashboard", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_errCodes_logn(self):
        ''' Test the error codes for unauthorized login '''
        loginResponse = self.login("Roland","2222");
        self.assertEqual(loginResponse.status_code, 403);

    def test_restApi(self):
        ''' Register and login user , try to buy 1 bitcoin and check the results '''
        registerResponse = self.register("Roland","226268", "226268");
        self.assertEqual(registerResponse.status_code, 200)
        loginResponse = self.login("Roland","226268")
        self.assertEqual(loginResponse.status_code, 200)

        buyResponse = self.app.post("/api/coins", 
        data = json.dumps({
            "coin":"bitcoin",
            "quantity": 1
        }, indent=4),
        headers= {
            "content-type": "application/json"
        }
        )

        walletResponse = self.app.get("/api/wallet");
        self.assertEqual(walletResponse.status_code, 200)
        self.assertEqual(walletResponse.get_json()["bitcoin"], 1)
        



if __name__ == "__main__":
    unittest.main()