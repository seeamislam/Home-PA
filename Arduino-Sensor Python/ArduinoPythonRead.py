# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 12:37:04 2019

@author: Anando Zaman
"""

import serial
from datetime import datetime
import pyrebase
from datetime import timedelta

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

arduino = serial.Serial('COM3', 9600, timeout=.1)
dataold = 'closed'
while True:
    data = arduino.readline()[0:-2] #the last bit gets rid of the new-line chars
    data = data.decode().strip()
    
    #Saves the time and state when door is opened
    if (data == 'open'):
        Timestamp = datetime.now()
        print("Door opened at " + Timestamp.strftime("%Y-%m-%d %H:%M:%S"))
        DoorState = db.child("Users").update({"Door":"opened at " + Timestamp.strftime("%Y-%m-%d %H:%M:%S")}) #Used to Change name value
        