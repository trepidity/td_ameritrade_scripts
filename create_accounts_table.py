import sqlite3
import os

conn = sqlite3.connect(os.environ.get('DB_NAME'))
conn.execute('''CREATE TABLE accounts (date,type,accountId,accruedInterest,cashBalance,longOptionMarketValue,
liquidationValue,longMarketValue,availableFunds,buyingPower,dayTradingBuyingPower,equity,equityPercentage,
longMarginValue,maintenanceRequirement,marginBalance)''')

conn.commit()
conn.close()
