import os
import pprint
import sqlite3

pp = pprint.PrettyPrinter()

conn = sqlite3.connect(os.environ.get('DB_NAME'))
cur = conn.cursor()

# type,accountId,accruedInterest,cashBalance,longOptionMarketValue,
# liquidationValue,longMarketValue,availableFunds,buyingPower,dayTradingBuyingPower,equity,equityPercentage,
# longMarginValue,maintenanceRequirement,marginBalance
cur.execute('SELECT * from accounts limit 2')
rows = cur.fetchall()

yesterdaysAccruedInterest = rows[0][3]
yesterdaysBuyingPower = rows[0][8]
yesterdaysAvailableFunds = rows[0][9]
yesterdaysDayTradingBalance = rows[0][10]
yesterdaysEquity = rows[0][11]
yesterdaysMarginBalance = rows[0][15]
yesterdaysLiquidationBalance = rows[0][6]

accruedInterest = rows[1][3]
buyingPower = rows[1][8]
availableFunds = rows[1][9]
dayTradingBalance = rows[1][10]
equity = rows[1][11]
marginBalance = rows[1][15]
liquidationBalance = rows[1][6]

print("Accrued Interest.................", accruedInterest)
print("Buying Power.....................", buyingPower)
print("Available Funds..................", availableFunds)
print("Day trading balance..............", dayTradingBalance)
print("Equity...........................", equity)
print("Margin balance...................", marginBalance)
print("Liquidation balance..............", liquidationBalance)
print()
# print("Cash Balance Changed.............", round(float(rows[1][4])/float(rows[0][4]), 2), "%")
print("Day trading balance changed......", round(float(dayTradingBalance)/float(yesterdaysDayTradingBalance), 2), "%")
print("Equity changed...................", round(float(equity)/float(yesterdaysEquity), 2), "%")
print("Margin balance changed...........", round(float(marginBalance)/float(yesterdaysMarginBalance), 2), "%")
print("Liquidation balance changed......", round(float(liquidationBalance)/float(yesterdaysLiquidationBalance), 2), "%")
