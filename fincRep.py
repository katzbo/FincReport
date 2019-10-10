#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
import json
import sys
import subprocess
import charge
from charge import Charge

googleApiKey = "key=xxx"


class GooglePlacesApiImpl:
    """docstring for GooglePlacesApiImpl"""
    gSearchPlaceURL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    gGEtPlaceDetailsURL = "https://maps.googleapis.com/maps/api/place/details/json"

    def __init__(self, googleApiKey):
        self.googleApiKey = googleApiKey

    def getPlaceId(self, placeName):
        params = {'input': placeName,
                  'inputtype': "textquery", 'key': self.googleApiKey}
        data = getJsonResponse(self, gSearchPlaceURL, params)
        try:
            return data['candidates'][0]['place_id']
        except:
            raise ValueError(
                "Place id request failed with json error response: " + data.text)

    def getPlaceCategory(self, placeId):
        params = {"key": googleApiKey, "placeid": placeId}
        # print(r.text)
        data = getJsonResponse(self, gGEtPlaceDetailsURL, params)
        try:
            placeCategory = data['result']['types']
            print(placeCategory)
        except:
            raise ValueError(
                "Category request failed with json error response: " + data.text)

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
    category = ChargeCategory(charge.category)
    category.addCharge(charge)
    print("adding category " + category.name)
    categoryList.append(category)

class ChargeCategory:
    """docstring for ChargeCategory"""

    def __init__(self, name):
        self.name = name
        self.sum = 0
        self.charges = []

    def addCharge(self, charge):
        self.charges.append(charge)
        self.sum += charge.price


if __name__ == "__main__":
    if not os.path.exists("node_modules"):
        os.system("npm install")

    try:
        # get user, pass, bank
        user, password, bank = sys.argv[1:4]
        print("financial report start")
    except ValueError:
        print("Usage: python fincRep.py [user] [password] [bank]")
        print("bank could be one of: 'hapoalim', 'leumi', 'discount', 'otsarHahayal', 'visaCal', 'leumiCard', 'isracard', 'amex'")
        sys.exit(1)

    run_scrapper_cmd = "node index.js {} {} {}".format(user, password, bank)
    subprocess.check_call(run_scrapper_cmd, shell=True)
    # read expenses
    with open("accounts.json") as file:
        expenses = json.load(file)["accounts"][0]["txns"]
    for expense in expenses:
    	pr = Charge(expense)
    	print(pr)
