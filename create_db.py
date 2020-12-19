import sqlite3
import os

conn = sqlite3.connect(os.environ.get('DB_NAME'))

