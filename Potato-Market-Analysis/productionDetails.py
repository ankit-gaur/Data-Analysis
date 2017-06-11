from DbHandler.utility import pdsql,pdsqlparam
import pandas as pd
import matplotlib.pyplot as plt


fig= plt.figure()

def readDataFile():
	return pd.read_csv('yearWisePotatoProduction.csv')

def makeAllIndiaProductivityGraph():
	yearWiseProducion = getAllIndiaProduction()
	print(yearWiseProducion)
	plt.plot(yearWiseProducion)
	plt.show()

def getAllIndiaProduction():
	pdata = readDataFile()
	pdata = pdata[(pdata['year']!=2015)]
	pdata = pdata.sort_values('year')
	pdata['production'] = pdata['production']/10000
	pdata['area'] = pdata['area']/1000
	yearWiseProducion = pdata.groupby('year')[['production','area']].sum()
	yearWiseProducion['productivity'] = yearWiseProducion['production']/yearWiseProducion['area']
	return yearWiseProducion

def getStateProduction(state):
	pdata= readDataFile()
	pdata = pdata[pdata['state'] ==  state]
	pdata['production'] = pdata['production']/10000
	pdata['area'] = pdata['area']/1000
	pdata = pdata.sort_values('year')
	yearWiseProducion = pdata.groupby('year')[['production','area']].sum()
	yearWiseProducion['productivity'] = yearWiseProducion['production']/yearWiseProducion['area']
	return yearWiseProducion

def makeStateProductionGraph(state):
	yearWiseProducion = getStateProduction(state)
	plt1 = fig.add_subplot(211)
	plt1.plot(yearWiseProducion)
	plt1.set_title(state)
	plt2 = fig.add_subplot(212)
	plt2.plot(getAllIndiaProduction())
	plt2.set_title("All India Production")
	plt.show()


def showStates():
	pdata = readDataFile()
	pdata = pdata[pdata['year']!=2015]
	production = pdata.groupby('state')['production','area'].sum()
	production = production.sort_values('production', ascending = False)
	print production





print '''
		a.AllIndiaProduction
		b.StateProduction	
		c.Show States ordered by production
		'''

choice = raw_input()
if choice =='a':
	makeAllIndiaProductivityGraph()
elif choice =='b':
	state = raw_input('state>> ')
	makeStateProductionGraph(state)
elif choice == 'c':
	showStates()		


