import requests
import bs4
from bs4 import BeautifulSoup
import urllib2 
import string 
from requests import get
import re

url = "http://www.99acres.com/property-rates-and-price-trends-in-mumbai"
filename = "ShoppingMallCount.txt"
headers = { 'User-Agent' : 'Mozilla/5.0' }

def open_url(url):
    return requests.get(url).text  # returns html

def get_bsoup_object(html):
    return BeautifulSoup(html, "html.parser")  # returns soup (BeautifulSoup's




req = urllib2.Request(url, None, headers)
html = urllib2.urlopen(req).read()
soup = get_bsoup_object(html)
k = 0
total=0

for j in soup.findAll('div',attrs={'href':'javascript:void(0);'}):
    temp = str(j)
    num=0
    area_name = temp
    area_name = area_name[87:]
    ind1 = [m.start() for m in re.finditer(r",",area_name)][4]
    ind2 = [m.start() for m in re.finditer(r",",area_name)][5]
    ind1 += 1
    area_name = area_name[ind1+1:ind2-1]
    #area name from 99acres -> price data available
    
    k+=1

    url2="https://www.google.co.in/maps/search/Malls+in+"+area_name


    res2=requests.get(url2)
    Text=res2.text
    soup2=bs4.BeautifulSoup(res2.text,'html.parser');
    #span itemprop="address"

    #length=Text.count('[\"Shopping Mall\"')
    
    obj=re.compile(r'\"Shopping Mall')
    elems=obj.findall(Text)
    total+=len(elems)
    #print(len(elem))
    print(area_name+ str(len(elems)))
    with open(filename, 'a') as out:
            out.write(str(k) + ' ' + area_name +'   ' +str(len(elems))+'\n')

    '''
    try:
        #Using re,  find (space)km in text
        obj=re.compile(r'null,\[(\d*),\"((\d)*(\.)*(\d)*) km')
        Match_object=obj.search(Text)
        dist=Match_object.group(2) #first occurrence
        print(dist)

        with open(filename, 'a') as out:
            out.write(str(k) + '. ' + area_name +'   '  + dist +'km' +'\n')
    
    except:
        with open(filename, 'a') as out:
            out.write(str(k) + '. ' + area_name +'   '  + str( ) +'km' +'\n')
    '''  

print(total)  

