import requests
from bs4 import BeautifulSoup
import urllib2 
import string 
from requests import get
import re

url = "http://www.99acres.com/property-rates-and-price-trends-in-mumbai"
filename = "QvsP.txt"
headers = { 'User-Agent' : 'Mozilla/5.0' }

def open_url(url):
    return requests.get(url).text  # returns html

def get_bsoup_object(html):
    return BeautifulSoup(html, "html.parser")  # returns soup (BeautifulSoup's object)
    

def gen_int_lis(passed_lis):
        #take a list that contains null values(garbage) and return a pure list of 
	low_int = list()
	flag = 0
	num_str = ""
	for i in range(len(passed_lis)):	
		if flag == 0 and (passed_lis[i] == 'n' or passed_lis[i] == 'u' or passed_lis[i] == 'l' or passed_lis[i] == ','):
			continue
		elif flag == 0:
			flag = 1
			#means the first digit
		#print("num_str is ", num_str)
		if flag == 1 and passed_lis[i] == ',':
			flag = 0
			low_int.append(int(num_str))
			num_str = ""
		elif flag == 1:
			num_str += passed_lis[i]
	return low_int
	

req = urllib2.Request(url, None, headers)
html = urllib2.urlopen(req).read()
soup = get_bsoup_object(html)
k = 0
dic1 = {'0':'Jan-Mar','1':'Apr-Jun','2':'Jul-Sep','3':'Oct-Dec'}


for j in soup.findAll('div',attrs={'href':'javascript:void(0);'}):
	temp = str(j)
	num=0
	area_name = temp
	area_name = area_name[87:]
	ind1 = [m.start() for m in re.finditer(r",",area_name)][4]
	ind2 = [m.start() for m in re.finditer(r",",area_name)][5]
	ind1 += 1
	area_name = area_name[ind1+1:ind2-1]
    
    
	temp = temp[86:91]	
	
	if temp[len(temp)-1] == "'":
		num = int(temp[0:4])
	elif temp[len(temp)-1] == ',':
		num = int(temp[0:3])
	else:
		num = int(temp)
	k += 1
	print(str(k) + ". "+area_name)
	
	#num is location ids to be used in the url
	#generate url and scrape each time
	s = "http://www.99acres.com/do/pricetrends?building_id=0&loc_id=" + str(num) + "&prop_type=1&pref=S&bed_no=0"
	req2 = urllib2.Request(s, None, headers)
	html2 = urllib2.urlopen(req2).read()
	soup2 = get_bsoup_object(html2)
	#print(soup2.prettify())
	#print("\n\n")
	low_lis = soup2.find('input', {'id': 'priceTrendVariables'}).get('price30')
	temp_lis = str(low_lis)
	low_lis = list(low_lis)
	
	med_lis = soup2.find('input', {'id': 'priceTrendVariables'}).get('median')	
	med_lis = list(med_lis)
	
	high_lis = soup2.find('input', {'id': 'priceTrendVariables'}).get('price70')
	high_lis = list(high_lis)
	
	
	
	#construct list of low_range of integers without null
	low_int = list()
	low_int = gen_int_lis(low_lis)
	
	med_int = list()
	med_int = gen_int_lis(med_lis)
	
	high_int = list()
	high_int = gen_int_lis(high_lis)
	
	#get start year
	start_y = soup2.find('input', {'id': 'priceTrendVariables'}).get('startyear')
	start_y = int(start_y)
	
	#Find out the starting month/quarter
	null_str = soup2.find('input', {'id': 'priceTrendVariables'}).get('price30')
	null_str = str(null_str)
	null_str = null_str[:14]
	null_flag = 0
	
	
	if null_str[:4] == "null":
		null_flag = 1
		if null_str[5:9] == "null":
			null_flag = 2
			if null_str[10:14] == "null":
				null_flag = 3 
	#print("null_flag is ", null_flag)
	#print(null_str)		 
	#print(dic1[str(null_flag)])
	#print(temp_lis)
	
	#setting initial string pointer 
	
	s_ptr = 0
	
	if null_flag == 1:
		s_ptr = 5
	elif null_flag == 2:
		s_ptr = 10
	elif null_flag == 3:
		s_ptr = 15
	 		
	year = start_y
	qtr = null_flag
	cnt = 0
	i1 = s_ptr
	i2 = s_ptr
	with open(filename, 'a') as out:
			out.write(str(k) + ' ' + area_name + '\n\n') 
			
	#print("len of low_int is ", len(low_int))
	i = -1
	print(len(low_int))
	for j in range(len(low_lis)):
		
		if(i + 1 >= len(low_int)):
			break

		#print("i: ", i+2)
		#temp_lis is the string to be parsed

		
		
		temp_s = ""
		while temp_lis[i2] != ',':
			temp_s += temp_lis[i2]
			i2 += 1
			
		i2 += 1
		
		#we have a value with val characters
		
		
		#print("qtr: ",qtr)
		#print("temp_s is ",temp_s)
		if temp_s == "null":
			#print("null")
			qtr += 1
			
			if qtr == 4:
				qtr = 0
				year += 1
			continue
			
		else:
			#print("no-null")
			i += 1
			with open(filename, 'a') as out:
				out.write(str(low_int[i]) + '  ' + str(med_int[i]) + '  ' + str(high_int[i]) + '  ' + str(year) +  '  ' + dic1[str(qtr)]+'\n\n')
		
		
				
		
		qtr += 1
		if qtr == 4:
			qtr = 0
			year += 1
		
	
	
	

