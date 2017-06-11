from DbHandler.ProductionTableHandler import addData


file_ = open('yearWisePotatoProduction.csv','r')

datalist = []

isEven = False
for line  in file_:
	if isEven:
		isEven = False
		continue
	else:
		isEven = True	
	data = line.split(',')
	del data[4]	
	temp = data[4]
	data[4] = data[5]
	data[5] = temp
 	datalist += [tuple(data)]

addData(datalist)


