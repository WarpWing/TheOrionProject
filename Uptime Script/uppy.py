import os
import requests
import json 

link = "https://google.com"
r = requests.get(link)
print("The response is {rcode} and I find it to be epic".format(rcode=r.status_code))
