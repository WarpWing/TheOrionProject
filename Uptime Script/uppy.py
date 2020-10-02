import os
import requests
import json 

weblist = ["google.com", "sky.lea.moe"]

for x in weblist:
   r = requests.get('https://sky.shiiyu.moe')
   rcode = r.status_code
printf("The Response Code is {rcode} and it's beautiful")
