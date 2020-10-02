import os
import requests
import json 


link = input("Please enter a link to get information on: ")
r = requests.get(link)
print("The response is {rcode} and I find it to be quite interesting".format(rcode=r.status_code))
