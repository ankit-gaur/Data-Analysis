import pandas as pd
import sqlite3

def pdsql(db,query):
	conn  = sqlite3.connect(db)
	cursor  = conn.execute(query)
	qdata = cursor.fetchall()
	cols = [column[0] for column in cursor.description]
	data = pd.DataFrame.from_records(data = qdata, columns = cols)
	conn.close()
	return data

def pdsqlparam(db,query,params):
	conn  = sqlite3.connect(db)
	cursor  = conn.execute(query,params)
	qdata = cursor.fetchall()
	cols = [column[0] for column in cursor.description]
	data = pd.DataFrame.from_records(data = qdata, columns = cols)
	conn.close()
	return data

