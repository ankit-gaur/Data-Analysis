from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import staleness_of
import time
 


def wait_for_page_load(driver):
	timeout = 6
	old_page = driver.find_element_by_tag_name('html')
	yield
	WebDriverWait(driver, timeout).until(staleness_of(old_page))

def my_wait_for_page_load(driver):
	data = driver.page_source
	lenP = len(data)
	while True:
		time.sleep(0.4)#slow speed
		lenC = len(driver.page_source)
		if lenC == lenP:
			print "page loaded completely"
			break
		else :
			print "page is loading"
			lenP = lenC	

def addNotFoundState(state):
	file_ = open('statesNotFound.txt','a+')
	file_.write(state+"\n")
	file_.close()

def wait_for_element(driver,id):
	time.sleep(1)
	delay = 2 # seconds
	try:
	    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, id)))
	    print "Page is ready!"
	except TimeoutException:
	    print "Loading took too much time!"

def loadHome(driver):
	driver.get("http://agmarknet.nic.in/agnew/NationalBEnglish/DatewiseCommodityReport.aspx?ss=1")

def savePage(name,driver):
	page = driver.page_source
  	file_ = open('./pages/'+name+'.html', 'w')
	file_.write(page)
	file_.close()

def savePageCount(count):
	file_ = open('page_count','w')
	file_.write(count)
	file_.close()

def getPageCount():
	file_ = open('page_count','r')
	for line in file_:
		return int(line)		



def doesPageContain(driver,str):
	page = driver.page_source
	if str in page:
		return True
	else:
		return False	





months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
years = ['2003', '2004', '2005', '2006', '2007', '2008', '2009' , '2010' , '2011' , '2012', '2013', '2014', '2015', '2016', '2017']
states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttrakhand', 'West Bengal', 'Chandigarh',  'Delhi' ] 


# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

loadHome(driver)

counted =getPageCount()
count = 0
for year in years:
	#loadHome(driver)
	for month in months:
		#loadHome(driver)
		for state in states:
			count = count+1
			if count<=counted:
				continue

			success = False
			while not success:	
				try:
					if doesPageContain(driver,"Error"):
						loadHome(driver)
						continue
					yearSelect = Select(driver.find_element_by_id('cboYear'))
					yearSelect.select_by_value(year)
					print year
					if doesPageContain(driver,"Error"):
						loadHome(driver)
						continue
					wait_for_element(driver,'cboMonth')
					if doesPageContain(driver,"Error"):
						loadHome(driver)
						continue
					monthSelect = Select(driver.find_element_by_id('cboMonth'))
					monthSelect.select_by_value(month)
					print month
					if doesPageContain(driver,"Error"):
						loadHome(driver)
						continue
					wait_for_element(driver,'cboState')
					if doesPageContain(driver,"Error"):
						loadHome(driver)
						continue
					stateSelect = Select(driver.find_element_by_id('cboState'))		
					print state 
					if doesPageContain(driver,state):
						if state == 'Delhi':
							state = 'NCT of Delhi'
						if doesPageContain(driver,"Error"):
							loadHome(driver)
							continue	
						stateSelect.select_by_value(state)
						if doesPageContain(driver,"Error"):
							loadHome(driver)
							continue
						wait_for_element(driver,'cboCommodity')	
						if doesPageContain(driver,"Error"):
							loadHome(driver)
							continue
						commoditySelect = Select(driver.find_element_by_id('cboCommodity'))
						if doesPageContain(driver,'Potato'):
							print "page contains potato"
							commoditySelect.select_by_visible_text('Potato') 
							if doesPageContain(driver,"Error"):
								loadHome(driver)
								continue
							wait_for_element(driver,'btnSubmit')
							if doesPageContain(driver,"Error"):
								loadHome(driver)
								continue
							btn = driver.find_element_by_id('btnSubmit')
							btn.click()
							if(doesPageContain(driver,"Data Not Reported")):
								savePageCount(str(count))
								success = True
								continue
							wait_for_element(driver,'gridRecords')
							#time.sleep(2)
							#wait_for_page_load(driver)
							my_wait_for_page_load(driver)
							savePage(year+'_'+month+'_'+state,driver)
							savePageCount(str(count))
							loadHome(driver)
							success =True
						else:
							print 'page does not contain potato'
							success =True	
					else:
						print 'page does not contain '+ state
						addNotFoundState(state)
						success = True
					success  = True	
				except NoSuchElementException:
					success  = False	
				except WebDriverException:
					successs = False		
			
			# 	continue	
			# try:
			# 	stateSelect.select_by_value(state)
			# 	wait_for_element(driver,'cboCommodity')
			# 	try:
			# 		commoditySelect = Select(driver.find_element_by_id('cboCommodity'))
			# 		commoditySelect.select_by_value('Potato') 
			# 	except NoSuchElementException:
			# 		print 'no such element exception\n'
			# 		continue
			# except NoSuchElementException:
			# 	err = True
					
				



print getPageCount()

wait_for_element(driver, 'cboMonth')

monthSelect = Select(driver.find_element_by_id('cboMonth'))
monthSelect.select_by_value('January')


 

#driver.quit()