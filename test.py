
import pandas as pd

DF = pd.read_csv("YAHOO-INDEX_GSPC.csv")

#print DF.head()
test = DF[DF.Date == "2015-11-30"].Adj_Close
print test
print float(test)

#
#print DF[DF.Adj_Close == "2015-11-30"]










