# You are given following list of stocks and their prices in last 3 days,

# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]
# 
# i. Write a program that asks user for operation. Value of operations could be,
#    a. print: When user enters print it should print following,
#       info ==> [600, 630, 620] ==> avg:  616.67
#       ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#       mtl ==> [234, 180, 160] ==> avg:  191.33
#    b. add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your  dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

import statistics

def printSP(StockPrices):
    for stocks,prices in StockPrices.items():
        print(f"{stocks}==>{prices}==>{round(statistics.mean(prices),2)}")

def add(StockPrices):
    ...



StockPrices={
    'info':[600,630,620],
    'ril':[1430,1490,1567],
    'mtl':[234,180,160]
}

printSP(StockPrices)

# operation=input("Enter the operation you want to commit : a.print b.add")
# if(operation.lower()=='print'):
#     printSP(StockPrices)
# elif(operation.lower()=='add'):
#     add(StockPrices)
# else:
#     print("INVALID CHOICE TRY AGAIN")