import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from DbHandler.utility import pdsql,pdsqlparam

sp = '   '
priceData = ''
months = ['','Jan','Feb','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']


def getPDataFrame():
	pdata = pd.read_csv('PriceData.csv')

def showDetails1(index):
	days = priceData['day']
	month = priceData['month']
	year = priceData['year']
	prices = priceData['modal_price']
	quantities = priceData['quantity']
	print str(days[index]) +  sp + months[int(month[index])] +sp + str(year[index])+ sp  + str(prices[index]) + sp + str(quantities[index]) + ' tonnes'


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


def getMandiPrices(mandi):
	global priceData
	priceData = pdsqlparam('PotatoData.db','select * from prices where mandi = ? order by year,month,day asc',(mandi,))
	prices = priceData['modal_price']
	return prices


def plotMandi(mandi):
	global priceData
	priceData = pdsqlparam('PotatoData.db','select * from prices where mandi = ? order by year,month,day asc',(mandi,))
	prices  = getMandiPrices(mandi)
	fig  = plt.figure()
	plt1 = fig.add_subplot(111)
	plt1.plot(range(len(prices)),prices,picker = True)
	#plt1.scatter(range(len(prices)),prices,picker = True,s = 8)
	plt1.set_title('modal price '+mandi)
	fig.canvas.mpl_connect('pick_event',onPick1)
	fig.canvas.mpl_connect('motion_notify_event', onPlotHover1) 
	plt.show()


def makeCsv():
	priceData = pdsql('PotatoData.db','select state,mandi,day,month,year,quantity,min_price,max_price,modal_price from prices')
	priceData.to_csv('PriceData.csv')



mandi = raw_input('Enter Mandi Name :')
plotMandi(mandi)







