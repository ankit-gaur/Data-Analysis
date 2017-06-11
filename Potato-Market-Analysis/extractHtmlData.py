from BeautifulSoup import BeautifulSoup 
import urllib2

import os
from os import listdir
from os.path import isfile, join
from DbHandler.PriceTableHandler import FileAdder,clearPriceTable,getNumEntriesInPriceTable
import DbHandler.CookieHandler as cookies




def get_table_data(html):
   
	soup =  BeautifulSoup(html)
	data = []
	if "Error in data connection. Please try after some time." in str(html):
		return data
	table = soup.find('table', attrs={'id':'gridRecords'})
	if table is None:
		return data
	table_body = table.find('tbody')
	if table_body is None:
		return data
	rows = table_body.findAll('tr')
	if rows is None:
		return data
	for row in rows:
		cols = row.findAll('td')
		cols = [ele.text.strip() for ele in cols]
		data.append([ele for ele in cols if ele]) 
	return data	



def validate_row(row):
	if len(row)<=5:
		return row
	for i in row:
		if i == 'NR':
			return []		
	return row					


def makeDatabaseMultipleRowsList(tdata,state):
	data = []
	mandi = ''
	for row in tdata:
		row = validate_row(row)
		if len(row) == 7:
			mandi = row[0]
		if len(row) ==6 :
			row = [mandi]+row	
		if len(row)<=5:
			continue
		row = [state]+row		
		rowdb = [row[0],row[1]]
		date = str(row[2])
		dmy  = date.split('/')
		rowdb = rowdb + dmy
		rowdb = rowdb+ [row[3],row[5],row[6],row[7]]
		#print rowdb
		if len(rowdb)<9:
			continue
		data.append(tuple(rowdb))
        
	return data		
				




savedFilesCountKey = 'savedFiles'
currentRowInFileKey = 'currentRowInFile'

adder = FileAdder()

path = "/home/ankit/aawork/coding/pythonscripts/priceData/pages"
html_file_paths = [join(path,f) for f in listdir(path) if isfile(join(path, f))]
html_file_paths.sort(key=lambda s: os.path.getmtime(s))
file_names =[ f for f in listdir(path) if isfile(join(path, f))]
file_names.sort(key=lambda s: os.path.getmtime(join(path,s)))


for idx in range(0,len(html_file_paths)):
	html_file_path = html_file_paths[idx]	
	print html_file_path + " " + file_names[idx]
	html = urllib2.urlopen('file://'+html_file_path)
	print 'getting data'
	tdata = get_table_data(html)
	state = str(file_names[idx].split('_')[2].split('.')[0])
	tdata = makeDatabaseMultipleRowsList(tdata,state)
	#print str(tdata)
	print 'got data'
	adder.addMultipleRows(tdata)
		


	# print state
	# for row in tdata:
	# 	row = validate_row(row)
	# 	numCols = len(row)
	# 	if numCols == 7:
	# 		curMandi = str(row[0])
	# 		date = str(row[1])
	# 		quantity = int(float(row[2]))
	# 		variety = str(row[3])
	# 		minPrice = int(float(row[4]))
	# 		maxPrice = int(float(row[5]))
	# 		modalPrice = int(float(row[6]))
	# 	if numCols == 6:	
	# 		date = str(row[0])
	# 		quantity = int(float(row[1]))
	# 		variety  = str(row[2])
	# 		minPrice  = int(float(row[3]))
	# 		maxPrice = int(float(row[4]))
	# 		modalPrice = int(float(row[5]))
	# 	if(numCols<=5):
	# 		continue	
		#print 'writing '+str(row)	
		#adder.addRowInPriceTable(state,curMandi,date,quantity,variety,minPrice,maxPrice,modalPrice)
		#print 'row written'	

adder.closeConnection()		


