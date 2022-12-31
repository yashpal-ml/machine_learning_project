from flask import Flask
from housing.logger import logging

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    logging.INFO("We are testing the logger package code")
    return "Starting Machine Learning Project"


if __name__=="__main__":
    # app.run(host="0.0.0.0", port=7000, threaded=True,debug=True)
    # app.run(debug=True, port=7000, threaded=True)
    app.run(debug=True)