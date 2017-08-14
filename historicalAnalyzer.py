import pandas as pd
import os
import time
from datetime import datetime

path = "./intraQuarter"

def keyStats(gather="Total Debt/Equity (mrq)"):
    statsPath = path + "/_KeyStats"
    stockList = [x[0] for x in os.walk(statsPath)]
    df = pd.DataFrame(columns = ["Date",
                                 "Unix",
                                 "Ticker",
                                 "DE_Ratio",
                                 "Price",
                                 "StockPChange",
                                 "SP500",
                                 "SPPChange"])

    # Data from CSV
    sp500DF = pd.read_csv("YAHOO-INDEX_GSPC.csv")
    tickerList = []

    for eachDir in stockList[1:5]:
        eachFile = os.listdir(eachDir)
        ticker = (eachDir.split("/")[3]).upper()
        tickerList.append(ticker)

        startingStockValue = False
        startingSP500Value = False

        if len(eachFile) > 0:
            for file in eachFile:
                dateStamp = datetime.strptime(file,"%Y%m%d%H%M%S.html")
                unixTime = time.mktime(dateStamp.timetuple())
                filePath = eachDir+"/"+file
                source = open(filePath, "r").read()
                source = source.replace("\n","")

                try:
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split("</td>")[0])

                    try:
                        sp500DF_date = datetime.fromtimestamp(unixTime).strftime("%Y-%m-%d")
                        sp500_value = float(sp500DF[sp500DF.Date == sp500DF_date].Adj_Close)
                    except Exception as e:
                        sp500DF_date = datetime.fromtimestamp(unixTime-259200).strftime("%Y-%m-%d")
                        sp500_value = float(sp500DF[sp500DF.Date == sp500DF_date].Adj_Close)

                    try:
                        stockPrice = float(source.split("</small><big><b>")[1].split("</b>")[0])
                    except:
                        try:
                            stockPrice = float(source.split("</small><big><b>")[1].split("</b>")[0].split(">")[1].split("<")[0])
                        except:
                            stockPrice = float(source.split('<span class="time_rtq_ticker"><span id="yfs')[1].split(">")[1].split("<")[0])

                    #print "stock price: ",stockPrice," ticker: ", ticker

                    if not startingStockValue:
                        startingStockValue = stockPrice
                    if not startingSP500Value:
                        startingSP500Value = sp500_value

                    stockPChange = ((stockPrice - startingStockValue) / startingStockValue)*100
                    SP500PChange = ((sp500_value - startingSP500Value) / startingSP500Value)*100


                    #Calc Stock Price from web page
                    df = df.append({"Date":dateStamp,
                                    "Unix":unixTime,
                                    "Ticker":ticker,
                                    "DE_Ratio":value,
                                    "Price":stockPrice,
                                    "StockPChange":stockPChange,
                                    "SP500":sp500_value,
                                    "SPPChange":SP500PChange},ignore_index = True)

                except Exception as e:
                    pass

    save = gather.replace(" ","").replace("(","").replace(")","").replace("/","")+".csv"
    print save
    df.to_csv(save)


keyStats()



##print "failed ! looked for:", ticker, sp500DF_date, dateStamp, unixTime
