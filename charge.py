#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

class Charge:
    def __init__(self, jsonCharge):
        self.description = jsonCharge["description"].encode('utf8')
        self.type = jsonCharge["type"].encode('utf8')
        processedDate_str = jsonCharge["processedDate"].encode('utf8')
        self.processedDate = datetime.datetime.strptime(processedDate_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        date_str = jsonCharge["date"].encode('utf8')
        self.date = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.originalAmount = jsonCharge["originalAmount"]
        self.chargedAmount = jsonCharge["chargedAmount"]
        self.originalCurrency = jsonCharge["originalCurrency"].encode('utf8')
        self.status = jsonCharge["status"].encode('utf8')

    def __str__(self):
    	return "description: " + self.description + " chargedAmount: " + str(self.chargedAmount) + " processedDate: " + str(self.processedDate)
