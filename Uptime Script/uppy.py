import os
import requests
import json 

weblist = ["sky.shiiyu.moe", "sky.lea.moe"]

for x in weblist:
   r = requests.get('https://sky.shiiyu.moe')
   rcode = r.status_code
   print(rcode)
