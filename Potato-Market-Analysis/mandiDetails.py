import sqlite3
from DbHandler.utility import pdsql,pdsqlparam
import pandas as pd
import matplotlib.pyplot as plt

priceData = []
sp = '  '
months = ['','Jan','Feb','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']

def getDataFrame():
	global priceData
	priceData = pd.read_csv('PriceData.csv')
	return priceData

def showDetails1(index):
	days = priceData['day']
	month = priceData['month']
	year = priceData['year']
	prices = priceData['modal_price']
	quantities = priceData['quantity']
	print str(days[index])  +sp + str(year[index])+ sp  + str(prices[index]) + sp + str(quantities[index]) + ' tonnes'


def onPick1(event):
	ind = event.ind #ndarraytype
	showDetails1(ind[0])



px = 0
def onPlotHover1(event):
	global px
	x = int(event.xdata)
	if(x<0 or x is None):
		return
	y = int(event.ydata)
	if x is not None and px != x and x <= len(priceData['max_price']):
		showDetails1(x)
		px = x #to prevent continous fast log

def getMandisList():
	mdata = pdsql('PotatoData.db','select mandi from prices')
	mandis  = mdata['mandi']
	mandis = set(mandis)
	for mandi in mandis:
		print mandi



def getMandiListByQuantity():
	mdata = pdsql('PotatoData.db','select mandi from prices')
	mandis  = mdata['mandi']
	mandis = set(mandis)
	descList = []
	for mandi in mandis:
		data = pdsqlparam('PotatoData.db','select quantity from prices where mandi = ?',(mandi,))
		qdata = data['quantity']
		quantities = list(qdata)
		if(len(quantities)<=300): #less number of objervations
			continue
		avg = sum(quantities)/len(quantities)
		descList.append([mandi,avg])
	descList.sort(key = lambda x: x[1],reverse = True)
	file_ = open('mandis.csv','w')	
	strData= ''
	for item in descList:
		strData += item[0] + ', ' +str(item[1]) + '\n'
	file_.write(strData)
	file_.close()


def mandiPotatoVolume(mandi):
	pdata= getDataFrame()
	pdata = pdata[pdata['mandi'] == mandi]
	pdata = pdata.sort_values(['year','month','day'])
	quantities = pdata['quantity']
	fig  = plt.figure()
	plt1 = fig.add_subplot(111)
	#plt1.plot(range(len(quantities)),quantities,picker = True)
	plt1.scatter(range(len(quantities)),quantities,picker = True,s = 8)
	#fig.canvas.mpl_connect('pick_event',onPick1)
	#fig.canvas.mpl_connect('motion_notify_event', onPlotHover1) 
	plt.show()

def plotQuantityVsPrice(mandi):
	global priceData
	pdata = getDataFrame()
	pdata = pdata[(pdata['mandi'] == mandi)]
	pdata = pdata.sort_values(['year','month','day'])
	priceData = pdata
	pAndQ = pdata[['modal_price','quantity']]
	fig  = plt.figure()
	plt1 = fig.add_subplot(111)
	plt1.scatter(pAndQ['quantity'],pAndQ['modal_price'],picker = True)
	plt.show()

mandi = raw_input('mandi>> ')
mandiPotatoVolume(mandi)	


