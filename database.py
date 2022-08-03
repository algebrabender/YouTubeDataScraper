import pyrebase
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('db_api_key')

firebaseConfig = {
  "apiKey": api_key,
  "authDomain": "data-project-220801.firebaseapp.com",
  "databaseURL": "https://youtube-data-project-220801-default-rtdb.europe-west1.firebasedatabase.app/",
  "projectId": "youtube-data-project-220801",
  "storageBucket": "youtube-data-project-220801.appspot.com",
  "messagingSenderId": "1040982344166",
  "appId": "1:1040982344166:web:57b99b1e41b9de38de9627",
  "measurementId": "G-86FKKTFJHD"
};

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def database_update(data) -> None:
    dt = datetime.now()
    fmt = '%Y-%m-%d'

    current_data = db.child("Girls_Camera_Guide").get().val()

    if dt.strftime(fmt) in current_data:
      db.child("Girls_Camera_Guide").child(dt.strftime(fmt)).update(data)
      print("update")
    else:
      db.child("Girls_Camera_Guide").child(dt.strftime(fmt)).set(data)
      print("set")

def database_data() -> dict():
    current_data = db.child("Girls_Camera_Guide").get().val()

    data_dict = {
        "viewCount": list(), 
        "likeCount": list(), 
        "commentCount": list()
    }

    for idx, date in enumerate(current_data):
        data_dict["viewCount"].append(int(current_data[date]["viewCount"]))
        data_dict["likeCount"].append(int(current_data[date]["likeCount"]))
        data_dict["commentCount"].append(int(current_data[date]["commentCount"]))

    return data_dict