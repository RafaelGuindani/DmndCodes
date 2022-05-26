import jsonpickle
import time
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By as by
from webdriver_manager.chrome import ChromeDriverManager

# Open the Google Chrome browser and open the website
service = Service (executable_path = ChromeDriverManager ().install ())
chrome = wd.Chrome (service = service)
url = 'https://www.rpachallenge.com/'
chrome.get (url)
chrome.maximize_window ()
chrome.refresh ()
time.sleep (2)

# Xpath Label
start = '//button[normalize-space()="Start"]'
fname = '//input[@ng-reflect-name="labelFirstName"]'
lname = '//input[@ng-reflect-name="labelLastName"]'
cname = '//input[@ng-reflect-name="labelCompanyName"]'
ricompany = '//input[@ng-reflect-name="labelRole"]'
adr = '//input[@ng-reflect-name="labelAddress"]'
ema = '//input[@ng-reflect-name="labelEmail"]'
pnumber = '//input[@ng-reflect-name="labelPhone"]'
submit = '//input[@value="Submit"]'

# Click Start
st = chrome.find_element (by.XPATH, start)
st.click ()

while True:
    # Read Jsonpickle

    class RPA:

        @property
        def name(self):
            return self.__name

        @property
        def lastname(self):
            return self.__lastname

        @property
        def company(self):
            return self.__company

        @property
        def rolecompany(self):
            return self.__rolecompany

        @property
        def address(self):
            return self.__address

        @property
        def email(self):
            return self.__email

        @property
        def phoneNumber(self):
            return self.__phoneNumber


    with open ("challange.json") as arq:
        reaD = jsonpickle.decode (arq.read ())

        a = -1
        for i in range(10):
            a = a + 1
            challange = reaD [a]
            #First Name
            fN = chrome.find_element (by.XPATH, fname)
            fN.send_keys (challange.name)
            # Last Name
            lN = chrome.find_element (by.XPATH, lname)
            lN.send_keys (challange.lastname)
            # Company
            cN = chrome.find_element (by.XPATH, cname)
            cN.send_keys (challange.company)
            # Role Company
            riC = chrome.find_element (by.XPATH, ricompany)
            riC.send_keys (challange.rolecompany)
            # Address
            adR = chrome.find_element (by.XPATH, adr)
            adR.send_keys (challange.address)
            # Email
            eM = chrome.find_element (by.XPATH, ema)
            eM.send_keys (challange.email)
            # Phone Number
            pN = chrome.find_element (by.XPATH, pnumber)
            pN.send_keys (challange.phoneNumber)
            # Submit
            sbmit = chrome.find_element (by.XPATH, submit)
            sbmit.click ()
