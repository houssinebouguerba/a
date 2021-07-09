from pymongo import MongoClient
import gridfs
import os
from picamera.array import PiRGBArray
from picamera import PiCamera
import imutils
import time
import cv2

from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import dlib
import datetime
from pymongo import MongoClient
import pymongo
print(pymongo.version)
from random import random

import dns
#just to make sure we aren't crazy, check the filesize on disk:

#MongoClient("197.2.249.32", 27017, replicaSet='replSet')

from pymongo import MongoClient






client = MongoClient("mongodb://admin:admin@freecluster-shard-00-00-oqzix.mongodb.net:27017,freecluster-shard-00-01-oqzix.mongodb.net:27017,freecluster-shard-00-02-oqzix.mongodb.net:27017/test?ssl=true&replicaSet=FreeCluster-shard-0&authSource=admin&retryWrites=true&w=majority",serverSelectionTimeoutMS=2000)
    
db = client.test



db=client['personnes_ther']

fs = gridfs.GridFS( db )
#fileID = fs.put(open('/home/pi/Desktop/QRoundProgressBar-master/im0.jpg', 'rb') ,filename="image233344",temp=20)


file = fs.find_one({'filename': 'image2972466160442026'})
image = file.read()


img = np.fromstring(image, dtype='uint8')
img = cv2.imdecode(img, cv2.IMREAD_COLOR)
img = cv2.resize(img, (250, 250))
img = np.multiply(img, 1 / 255.0)

cv2.imshow('im',img)
cv2.waitKey()
cv2.destroyAllWindows()

