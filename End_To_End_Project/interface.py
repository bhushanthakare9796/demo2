from flask import Flask ,render_template ,jsonify,request

import config

from Project_app.utils import BostanHousing

app  = Flask(__name__)
@app.route("/") # HOME API
def hello_flask():
    print("Welcome to flask")
    return "Hello Python"

@app.route("/predict_price")
def get_predicted():
    CRIM = 1.38799
    ZN=0.0
    INDUS=8.14 
    CHAS=0.0
    NOX=0.538 
    RM=5.950
    AGE=82.0
    DIS=3.9900
    RAD=4.0
    TAX=307.0
    PTRATIO=21.0
    B=232.60
    LSTAT=27.71

    Bostan = BostanHousing(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    Predicted_Price = Bostan.get_predicted()

    return jsonify ({"Result": f"Predicted House price in Bostan is :{Predicted_Price}"})

if __name__ == "__main__":
    app.run()