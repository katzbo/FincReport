#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests
import os

googleApiKey = "key=xxx"

class GooglePlacesApiImpl:
    """docstring for GooglePlacesApiImpl"""
    gSearchPlaceURL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    gGEtPlaceDetailsURL = "https://maps.googleapis.com/maps/api/place/details/json"

    def __init__(self, googleApiKey):
        self.googleApiKey = googleApiKey

    def getPlaceId(self, placeName):
        params = {'input': placeName, 'inputtype': "textquery", 'key': self.googleApiKey}
        data = getJsonResponse(self, gSearchPlaceURL, params)
        try:
            return data['candidates'][0]['place_id']
        except:
            raise ValueError("Place id request failed with json error response: " + data.text)

    def getPlaceCategory(self, placeId):
        params = {"key": googleApiKey, "placeid": placeId}
        # print(r.text)
        data = getJsonResponse(self, gGEtPlaceDetailsURL, params)
        try:
            placeCategory = data['result']['types']
            print(placeCategory)
        except:
            raise ValueError("Category request failed with json error response: " + data.text)

    def getJsonResponse(self, url, params):
        r = requests.get(url=gGEtPlaceDetailsURL, params=params)
        return r.json()


def addChargeToCategory(charge):
    for category in categoryList:
        if category.name == charge.category:
            category.addCharge(charge)
            print("added " + charge.name)
            return
    print("adding charge " + charge.name)
    category = ChargeCatrgory(charge.category)
    category.addCharge(charge)
    print("adding category " + category.name)
    categoryList.append(category)


class Charge:
    def __init__(self, name, price, companyName, date):
        self.name = name
        self.price = price
        self.companyName = companyName
        self.date = date


class ChargeCatrgory:
    """docstring for ChargeCatrgory"""

    def __init__(self, name):
        self.name = name
        self.sum = 0
        self.charges = []

    def addCharge(self, charge):
        self.charges.append(charge)
        self.sum += charge.price


#categoryList = []
#charge1 = Charge("delek", 12, "paz", "12.2.84")
#addChargeToCategory(charge1)
#charge2 = Charge("delek", 34, "paz", "12.2.84")
#addChargeToCategory(charge2)
#print("the sum of category " + categoryList[0].name + " and sum " + str(categoryList[0].sum))
print("financial report start")
#os.system("webdriver-manager start &")

rows = os.system("protractor conf.js")

for row in rows:
    cols = row.find_elements_by_tag("td")
    charge = Charge(cols[0], cols[1], cols[2], cols[3], cols[4])
    addChargeToCategory(charge)
