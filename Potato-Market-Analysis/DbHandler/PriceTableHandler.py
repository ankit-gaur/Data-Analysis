import sqlite3


dbName = 'PotatoData.db'


class FileAdder:

	def __init__(self):
		self.conn = sqlite3.connect(dbName)

	def addRowInPriceTable(self,state, mandi, date, quantity, variety, minPrice, maxPrice, modalPrice):
		dmy = date.split('/')
		year = int(dmy[2])
		month = int(dmy[1])
		day = int(dmy[0])
		params  = (state,mandi,year,month,day,variety,quantity, minPrice,maxPrice, modalPrice)
		self.conn.execute("insert into prices (id,state,mandi,year,month,day, quantity,min_price,max_price,modal_price) values (null,?,?,?,?,?,?,?,?,?)",params)
		self.conn.commit()

	def addMultipleRows(self,data):
		self.conn.executemany("insert into prices (id,state,mandi,day,month,year, quantity,min_price,max_price,modal_price) values (null,?,?,?,?,?,?,?,?,?)",data)
		self.conn.commit()

	def closeConnenction(self):
		self.conn.close()	
		


	

def clearPriceTable():
	conn = sqlite3.connect(dbName)
	conn.execute("delete from prices where 1=1")
	conn.commit()
	conn.close()

def showTable():
	conn = sqlite3.connect(dbName)
	cursor =  conn.execute('select * from prices')
	rows  = cursor.fetchall()
	for row in rows:
		print row
	conn.close()


def showStates():
	conn = sqlite3.connect(dbName)
	cursor = conn.execute('select state from prices')
	rows  =  cursor.fetchall()
	for row in rows:
		print row	
	conn.close()		
