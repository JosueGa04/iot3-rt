import pyrebase

config = {
  "apiKey": "AIzaSyBKrxPa85j_vmcmb3jPiiYrupWv9QA30Jk",
  "authDomain": "iot2023-18838.firebaseapp.com",
  "databaseURL": "https://iot2023-18838-default-rtdb.firebaseio.com/",
  "storageBucket": "iot2023-18838.appspot.com"
}

firebase = pyrebase.initialize_app(config)