from flask import Flask, request, jsonify, make_response
import os
import dialogflow
import requests
import json

import serial
from datetime import datetime
import pyrebase
from datetime import timedelta

#Running FLask application on http://127.0.0.1:8888/
#Webhook for Home-PA chatbot
app = Flask(__name__)

config = {
          "apiKey": "AIzaSyBiIEeoG2gge1T3dJzkJZ1LMM-pulGNHZQ",
    "authDomain": "hackthenorth-52761.firebaseapp.com",
    "databaseURL": "https://hackthenorth-52761.firebaseio.com",
    "projectId": "hackthenorth-52761",
    "storageBucket": "",
    "messagingSenderId": "1074935392745",
    "appId": "1:1074935392745:web:b20168ec08be8cbd4d8378"
          }
          
firebase = pyrebase.initialize_app(config)

db = firebase.database()

# default route
@app.route("/")
def index():
    return "webhook"

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    #Doorstatus
    action = req.get('queryResult').get('action') #The action key from the JSON data extracted from DialogFlow has a key-value asociated with it. If not, then returns none.
    if action == "DoorStatus": #If json posts value is DoorStatus, then return the below JSON response for dialogflow to read
        print('Successful webhook access')
        GetDoorStatus = db.child("Users").child("Door").get().val()
        return {'fulfillmentText': GetDoorStatus}

    

    #Backyard Status
    action = req.get('queryResult').get('action')
    if action == "BackyardStatus":
        print('Successful webhook access')
        GetBackyardStatus = db.child("Users").child("Backyard-Activity").get().val()
        return {'fulfillmentText': GetBackyardStatus}



    #LightStatus
    action = req.get('queryResult').get('action')
    if action == "LightsStatus":
        print('Successful webhook access')
        LightsStatus = db.child("Users").child("Lights").get().val()
        return {'fulfillmentText': LightsStatus}



    #GarageStatus
    action = req.get('queryResult').get('action') #
    if action == "GarageStatus":
        print('Successful webhook access')
        GarageStatus = db.child("Users").child("GarageDoor").get().val()
        return {'fulfillmentText': GarageStatus}



    #FrontLawnActivity
    action = req.get('queryResult').get('action') 
    if action == "FrontLawnActivity": 
        print('Successful webhook access')
        FrontLawn = db.child("Users").child("Motion-Activity").get().val()
        return {'fulfillmentText': FrontLawn}


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))
    
    
if __name__=='__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug=True
    app.run(host = '0.0.0.0',port=8888)
