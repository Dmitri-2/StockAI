import pandas as pd
import os
import time
from datetime import datetime

path = "./intraQuarter"

def keyStats(gather="Total Debt/Equity (mrq)"):
    statsPath = path + "/_KeyStats"
    stockList = [x[0] for x in os.walk(statsPath)]
    df = pd.DataFrame(columns = ["Date","Unix","Ticker","DE Ratio", "Price","SP500"])
    timeBack = 86400

    # Data from CSV
    sp500DF = pd.read_csv("YAHOO-INDEX_GSPC.csv", nrows=1000000)


    for eachDir in stockList[1:5]:
        eachFile = os.listdir(eachDir)
        ticker = (eachDir.split("/")[3]).upper()

        if len(eachFile) > 0:
            for file in eachFile:
                dateStamp = datetime.strptime(file,"%Y%m%d%H%M%S.html")
                unixTime = time.mktime(dateStamp.timetuple())
                # print (dateStamp, unixTime)

                filePath = eachDir+"/"+file
                source = open(filePath, "r").read()
                try:
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split("</td>")[0])
                    try:
                        sp500DF_date = datetime.fromtimestamp(unixTime).strftime("%Y-%m-%d")
                        row= sp500DF['Adj Close'][(sp500DF['ticker']==str(ticker.upper())) & (sp500DF['date']==str(sp500DF_date))]
                        sp500_value = float(row)
                    except:
                        while sp500DF['Adj Close'][(sp500DF['ticker']==str(ticker)) & (sp500DF['date']==str(sp500DF_date))].empty:
                            sp500DF_date = datetime.fromtimestamp(unixTime - timeBack).strftime("%Y-%m-%d")
                            timeBack += 86400
                            if timeBack > 604800:
                                break

                        row= sp500DF['Adj Close'][(sp500DF['ticker']==str(ticker.upper())) & (sp500DF['date']==str(sp500DF_date))]
                        sp500_value = float(row)

                    #Calc Stock Price from web page

                    df = df.append({"Date":dateStamp,
                                    "Unix":unixTime,
                                    "Ticker":ticker,
                                    "DE Ratio":value,
                                    "Price":0},ignore_index = True)
                except Exception as e:
                    print "failed ! looked for:", ticker, sp500DF_date, dateStamp, unixTime
                    pass
    save = gather.replace(" ","").replace("(","").replace(")","").replace("/","")+".csv"
    print save
    df.to_csv(save)


keyStats()



# row = sp500DF['Adj Close'][(sp500DF['ticker']=='A') & (sp500DF['date']=='1999-11-24')]
# print float(row)
# time.sleep(5);
# row= sp500DF['Adj Close'][(sp500DF['ticker']=="A") & (sp500DF['date']=="1999-11-24")]
# sp500_value = float(row)
# print "sp 500 value is: ", sp500_value
# time.sleep(5)
