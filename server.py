from flask import Flask,jsonify
from vijay import shivu 

app=Flask(__name__)

@app.route("/mithun",methods=["GET"])
def  mithun():
    pradeep=shivu()
    return jsonify({"college":pradeep})
    

if __name__=="__main__":
    app.run(debug=True,port=5001)
