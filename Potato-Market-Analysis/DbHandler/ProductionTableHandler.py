import sqlite3



dbName = 'PotatoData.db'

def connect():
	return sqlite3.connect(dbName)


def addData(data):
	'''
	data is list of tuples containing query params
	'''
	conn = connect()
	conn.executemany('insert into production (id,state,place,year,session,production,area) values (null,?,?,?,?,?,?)',data)
	conn.commit()
	conn.close()


def statesList():
	conn = connect()
	cursor = conn.execute('select state from production')
	stateList = [data[0] for data in cursor.fetchall()]
	stateSet = set(stateList)
	print str(stateSet)
	conn.close()
	return stateSet


def productionSum(year):
	conn = connect()
	cursor = conn.execute('select production from production where year = ?',(year,))
	pdata = cursor.fetchall()
	# totalproduction = sum(pdata)
	totalproduction = 0
	for data in pdata:
		totalproduction  += data[0]
	conn.close()	
	return totalproduction	



def areaSum(year):
	conn = connect()
	cursor = conn.execute('select area from production where year = ?',(year,))
	adata = cursor.fetchall()
	totalArea = 0
	for data in adata:
		totalArea += data[0] #data is tuple, adata is list of tuple
	conn.close()	
	return totalArea



def productivity(year):
	return productionSum(year)/areaSum(year)


def stateProduction(state,year):
	conn = connect()
	cursor = conn.execute('select production from production where state = ? and year = ?',(state,year,))
	pdata = cursor.fetchall()
	totalproduction = 0
	for data in pdata:
		totalproduction  += data[0]
	conn.close()	
	return totalproduction

def stateArea(state,year):
	conn = connect()
	cursor = conn.execute('select area from production where state =  ? and year = ?',(state,year,))
	adata = cursor.fetchall()
	totalArea = 0
	for data in adata:
		totalArea += data[0] #data is tuple, adata is list of tuple
	conn.close()	
	
	;fdsyui
	eturn totalArea	

def stateProductivity(state,year):
	return stateProduction(state,year)/stateArea(state,year)


def clearTable():
	conn  = connect()
	conn.execute('delete from production where 1=1')
	conn.commit()
	conn.close()

 