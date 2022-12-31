from flask import Flask
import sys
from housing.exception import HousingException
from housing.logger import logging

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise("We are raising custom exception")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.INFO(housing.error_message)
        logging.INFO("We are testing the logger package code")
    return "Starting Machine Learning Project"


if __name__=="__main__":
    # app.run(host="0.0.0.0", port=7000, threaded=True,debug=True)
    # app.run(debug=True, port=7000, threaded=True)
    app.run(debug=True)