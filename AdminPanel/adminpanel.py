import npyscreen
import json
import os
import sys
import requests  
from apfunc import * 

class sop(npyscreen.NPSApp):
    def main(self):
        # This reference the main GUI and can call functions from apfunc
        F  = npyscreen.Form(name = "Welcome to the Sentinel Overwatch Program",) 
        dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        
        F.add(npyscreen.TitleText, name="Placeholder Text")
        F.edit()

if __name__ == "__main__":
    App = sop()
    App.run()