#!/usr/bin/env python
# coding: utf-8

# In[4]:


import urllib.request
import uuid
import os, re, os.path

mypath = "DailyUpdated"
for root, dirs, files in os.walk(mypath):
    for file in files:
        os.remove(os.path.join(root, file))

for x in range(2):
    print(x)
#     urllib.request.urlretrieve("https://picsum.photos/4000/2000", "loreum/{}.jpg".format(uuid.uuid1()))
    urllib.request.urlretrieve("https://unsplash.it/1920/1080?random", "DailyUpdated/{}.jpg".format(uuid.uuid1()))
    
    


# In[ ]:


import uuid
uuid.uuid1()


# In[11]:


for x in range(6):
  print(x)


# In[ ]:




