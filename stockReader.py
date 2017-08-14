import pandas_datareader.data as web

q = web.get_quote_google(['AGNC', 'ADP'])

print q






#import csv
#import sys
#
#f = open("HistoricalQuotes.csv", "r")
#reader = csv.reader(f);
#print reader
#for row in reader:
#    print row
#
#f.close()
