import sqlite3
from sys import argv

script, dbName,tableName = argv

connection = sqlite3.connect(dbName)
cursor = connection.execute('select * from ' + tableName)
names = [description[0] for description in cursor.description]
connection.close()
print names