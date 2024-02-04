# stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
# pe ratio = price / earnings per share
# price to book ratio = price / book value

# Your input format (stocks.csv) is,

# Company Name	Price	Earnings Per Share	Book Value
# Reliance	    1467	    66	                653
# Tata Steel	391	        89	                572

# Output.csv should look like this,

# Company Name	PE Ratio	PB Ratio
# Reliance	    22.23	       2.25
# Tata Steel	4.39	       0.68

# {'Company Name': 'Reliance', 'Price': '1467', 'Earnings Per Share': '66', ' Book Value': '653'}


import csv

newDict={}
with open('Exercise/stocks.csv','r') as f:
    fDict=csv.DictReader(f)
    for row in fDict:
        for key,value in row.items():
            print()