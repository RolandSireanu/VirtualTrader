from .. import ProcesessRequest
from .. import app
from flask import request, redirect, make_response, jsonify, url_for, session


@app.route("/api/coins", methods=["POST"])
@app.route("/api/coins/<int:stock_id>", methods=["DELETE"])
def coinsEndpoint(stock_id=None):

    if(request.method == "POST"):
        if(request.is_json):
            if(request.cookies.get("tooken") == session.get("tooken")):
                data = request.get_json();
                print(data)                
                ProcesessRequest.Transaction(data["coin"], session["user"], int(data["quantity"]), "buy");
                return make_response(jsonify({"message":"success"}), 200);
            else:
                return make_response(jsonify({"message":"Please log in first"}), 400)
        else:
            return make_response(jsonify({"message":"Request doesn't contain json !"}),400);
    elif(request.method == "DELETE"):
        if(request.is_json):
            if(request.cookies.get("tooken") == session.get("tooken")):
                data = request.get_json();
                ProcesessRequest.Transaction(data["coin"], session["user"], int(data["quantity"]), "sell", pricePaid=data["pricePaid"], transactionId=stock_id);    
                return make_response(jsonify({"message":"success"}), 200);
    else:
        print("Operation not supported !");


@app.route("/api/wallet", methods=["GET"])
def walletEndpoint():
    if(request.cookies.get("tooken") == session.get("tooken")):
        crypto = ProcesessRequest.GetCryptoFromDB(session["user"]);
        return make_response(jsonify(crypto), 200);

    return make_response(400);
