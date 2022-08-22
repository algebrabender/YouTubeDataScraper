import pyrebase
from datetime import datetime
from dotenv import load_dotenv
import os
import pytz

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
  "measurementId": "G-86FKKTFJHD",
  "serviceAccount": "youtube-data-project-220801-firebase-adminsdk-30od9-8c0994402d.json"
};

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def database_update(title, data) -> None:
    tz_Seo = pytz.timezone('Asia/Seoul') 
    dt_Seo = datetime.now(tz_Seo)
    fmt = '%m-%d'

    db_data = db.get().val()

    if title not in db_data.keys():
        db.child(title).child(dt_Seo.strftime(fmt)).set(data)
        return

    current_data = db.child(title).get().val()
    
    if dt_Seo.strftime(fmt) in current_data:
      db.child(title).child(dt_Seo.strftime(fmt)).update(data)
      # print("update")
    else:
      db.child(title).child(dt_Seo.strftime(fmt)).set(data)
      # print("set")

def database_data(video) -> dict():
    data = db.get().val()
    if video in data.keys():
        current_data = db.child(video).get().val()
    else:
        return None

    data_dict = {
        "date": list(),
        "viewCount": list(), 
        "likeCount": list(), 
        "commentCount": list()
    }

    for idx, date in enumerate(current_data):
        data_dict["date"].append(date)
        data_dict["viewCount"].append(int(current_data[date]["viewCount"]))
        data_dict["likeCount"].append(int(current_data[date]["likeCount"]))
        data_dict["commentCount"].append(int(current_data[date]["commentCount"]))

    return data_dict

def database_keys() -> list():
    vals = db.get().val();
    keys = []
    
    for idx, val in enumerate(vals):
        if val != "video_ids":
          keys.append(val)
    
    return keys

def database_update_video_ids(title, video_id):
    db.child("video_ids").child(title).set(video_id)

def database_video_ids(title):
    return db.child("video_ids").child(title).get().val()