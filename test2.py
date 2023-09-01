from datetime import date, datetime, timedelta  # import libraries required for working with date and time
import re
import os
import csv
import pyodbc
import sqlite3

# conn = sqlite3.connect('sqlite.db')
conn = pyodbc.connect('Driver=SQLite3 ODBC Driver;Database=sqlite.db')
cur = conn.cursor()

# cur.execute('CREATE TABLE News (city, text, datetime)')
# cur.commit()
# cur.execute('CREATE TABLE PrivateAd (text, untildate, daysleft)')
# cur.commit()
# cur.execute('CREATE TABLE Necrologue (text, name)')
# cur.commit()


# cur.execute('DROP TABLE News')
# cur.commit()
# cur.execute('DROP TABLE PrivateAd')
# cur.commit()
# cur.execute('DROP TABLE Necrologue')
# cur.commit()

cur.execute('select * from News')
result = cur.fetchall()
print(result)
cur.execute('select * from PrivateAd')
result = cur.fetchall()
print(result)
cur.execute("select * from Necrologue")
result = cur.fetchall()
print(result)


cur.close()
conn.close()
