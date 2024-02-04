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
# {'Company Name': 'Tata Steel', 'Price': '391', 'Earnings Per Share': '89', ' Book Value': '572'}
# {'Company Name': 'Infosys', 'Price': '650', 'Earnings Per Share': '35', ' Book Value': '147'}
# {'Company Name': 'Axis Bank', 'Price': '739', 'Earnings Per Share': '19', ' Book Value': '263'}
# {'Company Name': 'Bajaj Finance', 'Price': '4044', 'Earnings Per Share': '69', ' Book Value': '341'}


import csv

newDict={}
final={}
with open('Exercise/stocks.csv','r') as f:
    fDict=csv.DictReader(f)
    for row in fDict:
        
        PERation=int(row['Price'])/int(row['Earnings Per Share'])
        PBRation=int(row['Price'])/int(row[' Book Value'])
            
        newDict['Company Name']=row.get('Company Name')
        newDict['PE Ratio']=round(PERation,2)
        newDict['PB Ratio']=round(PBRation,2)
        final.update(newDict)
        print(newDict)
        
        fieldnames=['Company Name','PE Ratio','PB Ratio']
        with open('Exercise/output.csv','w') as fw:
            
            csv_writer=csv.DictWriter(fw,fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(newDict)
            