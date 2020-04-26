import urllib.request
import uuid
import os, re, os.path

mypath = "DailyUpdated"
for root, dirs, files in os.walk(mypath):
    for file in files:
        os.remove(os.path.join(root, file))

for x in range(10):
    print(x)
    urllib.request.urlretrieve("https://unsplash.it/1920/1080?random", "DailyUpdated/{}.jpg".format(uuid.uuid1()))




