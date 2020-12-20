import os
import pprint
import sqlite3
from datetime import datetime
from datetime import timedelta
from td.client import TDClient

# Start_date initialized to none to pull all records
start_date = ''

pp = pprint.PrettyPrinter()
conn = sqlite3.connect(os.environ.get('DB_NAME'))

cur = conn.cursor()
cur.execute('SELECT MAX(transactionDate) FROM transactions limit 1')
row = cur.fetchone()
if row[0] is not None:
    start_date = (datetime.strptime(row[0], "%Y-%m-%dT%H:%M:%S+0000") + timedelta(days=1)).strftime("%Y-%m-%d")

# Create a new session, credentials path is required.
TDSession = TDClient(
    client_id=os.environ.get('CLIENT_ID'),
    redirect_uri='https://localhost/callback',
    credentials_path='td_credentials.json'
)

# Login to the session
TDSession.login()

# get transactions. If first run, start_date is empty.
transaction_data_multi = TDSession.get_transactions(
    account=os.environ.get('ACCOUNT_ID'),
    transaction_type='TRADE',
    start_date=start_date
)


def key_val(element, name):
    try:
        return element[name]
    except KeyError:
        if name == 'underlyingSymbol':
            return element['symbol']

        return ''


# type, subAccount, orderId, netAmount, transactionDate, orderDate, transactionSubType, transactionId, amount, price,
# cost, symbol, underlyingSymbol, optionExpirationDate, putCall, cusip, assetType
for key in transaction_data_multi:
    tItem = key['transactionItem']
    print(tItem)
    instrItem = tItem['instrument']
    conn.execute('insert into transactions values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [
        key_val(key, 'type'),
        key_val(key, 'subAccount'),
        key_val(key, 'orderId'),
        key_val(key, 'netAmount'),
        key_val(key, 'transactionDate'),
        key_val(key, 'orderDate'),
        key_val(key, 'transactionSubType'),
        key_val(key, 'transactionId'),
        key_val(tItem, 'amount'),
        key_val(tItem, 'price'),
        key_val(tItem, 'cost'),
        key_val(instrItem, 'symbol'),
        key_val(instrItem, 'underlyingSymbol'),
        key_val(instrItem, 'optionExpirationDate'),
        key_val(instrItem, 'putCall'),
        key_val(instrItem, 'cusip'),
        key_val(instrItem, 'assetType')])

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

print("Total records returned.....", len(transaction_data_multi))
