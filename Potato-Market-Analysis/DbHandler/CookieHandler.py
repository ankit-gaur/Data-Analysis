import sqlite3


dbname = 'Cookies.db'
tableName = 'cookies'

def connect():
	return sqlite3.connect(dbname)

def createCookieTable():
	conn = connect()
	conn.execute('create table cookies (key text primary key not null, value text  not null);')
	conn.commit()
	conn.close()

def isKeyExist(key):
	conn = connect()
	params = (key,)
	cursor =  conn.execute('select * from cookies where key = ?',params)
	isExist = len(cursor.fetchall())>0
	conn.close()
	return isExist

def saveCookie(key, value):
	value = str(value)
	conn = connect()
	if isKeyExist(key):
		conn.execute('update cookies set value = ? where key = ?',(value,key,))
		conn.commit()
	else:
		conn.execute('insert into cookies (key,value) values (?, ?)',(key,value,))
		conn.commit()
	conn.close()

def getCookie(key):
	conn = connect()
	cursor = conn.execute('select value from cookies where key = ?',(key,))
	value = cursor.fetchone()[0]
	conn.close()
	return value	

def deleteAllCookies():
	conn  = connect()
	cursor = conn.execute('delete from cookies where 1 =1')
	conn.commit()
	conn.close()		

