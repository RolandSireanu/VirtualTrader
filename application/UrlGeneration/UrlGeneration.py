from .. import app;
from itsdangerous import TimestampSigner
from flask import url_for

class UrlGeneration : 

    saltReset = "reset-password";
    lifeTime = 1200
    signer = TimestampSigner(secret_key=app.config.get("SECRET_KEY"), salt=saltReset);

    def __init__(self):
        pass    

    def signEmail(self, email):
        # signer = TimestampSigner(secret_key=app.config.get("SECRET_KEY"), salt=UrlGeneration.saltReset);
        tokenUrl = UrlGeneration.signer.sign(email);
        tempUrl = str(url_for("resetPasswordWithToken",token=tokenUrl.decode("utf-8"), _external=True));
        return tempUrl;

    def unsignEmail(self, link):
        if(UrlGeneration.signer.validate(link, max_age=UrlGeneration.lifeTime)):
            try:
                result = UrlGeneration.signer.unsign(link);
            except:
                print("UrlGeneration unsign failed ");
            return result.decode("utf-8");
        else:
            return None;

    def getOriginalEmail(self, token):

        # return urlSerializer.loads(token, salt="recover-key");
        pass