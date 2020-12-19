import sqlite3
import os

conn = sqlite3.connect(os.environ.get('DB_NAME'))
conn.execute('''CREATE TABLE transactions (type, subAccount, orderId, netAmount, transactionDate, orderDate, 
transactionSubType, transactionId, amount, price, cost, symbol, underlyingSymbol, optionExpirationDate, putCall, 
cusip, assetType)''')
