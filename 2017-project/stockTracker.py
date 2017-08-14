import pandas as pd
import pandas_datareader.data as web
import os
import time
from datetime import datetime
import csv
#import requests_cache


# f = open("../Transactions.csv", "r")
# reader = csv.reader(f);
# print reader
# for row in reader:
#    print row
#    f.close()
#    time.sleep(15)

class Stock():
    def getCurrentPrice(self):
        # q = web.get_quote_google(['AGNC'])
        # print q["last"]["AGNC"]
        return 25.12

    def __init__(self, ticker, buyPrice, currentPrice, shares, date):
        self.ticker = ticker
        self.buyPrice = buyPrice
        self.currentPrice = self.getCurrentPrice()
        self.shares = shares
        self.timestamp = date.today()

    def display(self):
        print "Ticker: ".ljust(16) + str(self.ticker)
        print "Buy Price: ".ljust(15),self.buyPrice
        print "Current Price: ".ljust(15),self.currentPrice
        print "Purchase Date: ".ljust(15),self.timestamp

    def displayProfit(self):
        margin = self.currentPrice - self.buyPrice
        percent = (margin/self.currentPrice)*100
        net = "gain"
        if margin < 0:
            net = "loss"
        print "Margin: ".ljust(15),margin," at a percent", net,"of %",percent

    def calcPercent(self):
        margin = self.currentPrice - self.buyPrice
        percent = (margin/self.currentPrice)*100
        return percent

    def setShares(self, number):
        self.shares = number;

    def getTotalValue(self):
        return self.shares*self.currentPrice

    def stringify(self):
        return self.ticker+"-"+str(self.buyPrice)+"-"+str(self.currentPrice)+"-"+str(self.shares)

class StockManager():
    def restoreData(self):
        fileIn = open("StockManager.txt", "r")
        fileData = fileIn.read()
        fileData = fileData.split("\n")
        loadedStocks = []
        for line in fileData:
            stockData=line.split("-")
            if line == "":
                break
            ticker=stockData[0]
            buyPrice=float(stockData[1])
            currentPrice=float(stockData[2])
            shares=int(stockData[3])
            loadedStocks.append(Stock(ticker,buyPrice,currentPrice,shares,datetime))
        self.stocks=loadedStocks

    def __init__(self):
        self.restoreData()
    def addStock(self, Stock):
        self.stocks.append(Stock)
    def saveAllData(self):
        fileOut = open("StockManager.txt", "w+")
        for stock in self.stocks:
            fileOut.write(str(stock.stringify()))
            fileOut.write("\n")
        fileOut.close()

#Immutable Source Data
manager = StockManager()

manager.stocks[0].display()
manager.stocks[0].displayProfit()
manager.stocks[0].getCurrentPrice()
manager.saveAllData()
manager.restoreData()

















# manager.addStock(Stock("AGNC",21.92,21.45,5))
# manager.addStock(Stock("RSP",21.92,21.45,5))
# manager.addStock(Stock("HAHA",21.92,21.45,5))
# manager.addStock(Stock("AGNC",21.92,21.45,5))

# other = {'last' : pd.Series([21.45], index=['AGNC'])}
# other = pd.DataFrame(other)
#
# #print q
