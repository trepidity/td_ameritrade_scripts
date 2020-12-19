import pprint
import os
import sqlite3
from td.client import TDClient

pp = pprint.PrettyPrinter()
conn = sqlite3.connect(os.environ.get('DB_NAME'))

# Create a new session, credentials path is required.
TDSession = TDClient(
    client_id=os.environ.get('CLIENT_ID'),
    redirect_uri='https://localhost/callback',
    credentials_path='td_credentials.json'
)

# Login to the session
TDSession.login()

# `get_transactions` Endpoint. Should not return an error
accounts = TDSession.get_accounts(account=os.environ.get('ACCOUNT_ID'))
a = accounts['securitiesAccount']
b = accounts['securitiesAccount']['currentBalances']
conn.execute('insert into accounts values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [a['type'], a['accountId'], b['accruedInterest'], b['cashBalance'], b['longOptionMarketValue'], b['liquidationValue'], b['longMarketValue'], b['availableFunds'], b['buyingPower'], b['dayTradingBuyingPower'], b['equity'], b['equityPercentage'], b['longMarginValue'], b['maintenanceRequirement'], b['marginBalance']])

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
