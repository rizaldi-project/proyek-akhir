import time
from picamera2 import Picamera2, Preview
import pyrebase

firebaseConfig = {
'apiKey': "AIzaSyDNLQuZJTrJjn7NpiDXy_XI-5I-Tv_4yDI",
'authDomain': "monitoring-meteran-pln.firebaseapp.com",
'databaseURL': "https://monitoring-meteran-pln-default-rtdb.asia-southeast1.firebasedatabase.app" ,
'projectId': "monitoring-meteran-pln",
'storageBucket': "monitoring-meteran-pln.appspot.com",
'messagingSenderId': "480750260460",
'appId': "1:480750260460:web:a97dcbd4bbf010fcd955c9",
'measurementId': "G-L4DCK5NQ2M"

}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

camera = PiCamera2()


