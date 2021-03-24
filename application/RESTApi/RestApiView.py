from .. import ProcesessRequest
from .. import app
from flask import request, redirect, make_response, jsonify, url_for, session


@app.route("/api", methods=["POST","GET"])
def buy():

    if(request.method == "POST"):
        if(request.is_json):
            if(request.cookies.get("tooken") == session.get("tooken")):
                data = request.get_json();
                print(data)
                ProcesessRequest.Transaction(data["coin"], float(data["price"]), session["user"], int(data["quantity"]), data["action"]);
            else:
                return make_response(jsonify({"message":"Please log in first"}), 400)
        else:
            print("Warning: request doesn't contain json !")
            return redirect(url_for("login"));
    elif(request.method == "GET"):
        #print(request.args.get("crypto"))
        if(request.cookies.get("tooken") == session.get("tooken")):
            crypto = ProcesessRequest.GetCryptoFromDB(session["user"]);
            return make_response(jsonify(crypto), 200);
            
        

    else:
        print("Warning: Unknown method !")
        
    
    r = make_response(jsonify({"message":"Everything is ok !"}), 200)
    res = make_response(redirect(url_for("dashboard")))

    return res;