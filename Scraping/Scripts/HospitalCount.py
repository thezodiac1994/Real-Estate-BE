import requests
import bs4
from bs4 import BeautifulSoup
import urllib2 
import string 
from requests import get
import re

#url = "http://www.99acres.com/property-rates-and-price-trends-in-mumbai"
filename = "HospitalCount.txt"
headers = { 'User-Agent' : 'Mozilla/5.0' }

with open('C:\\Users\\Sampath\\be-2\\Real-Estate-BE\\Scraping\\Scripts\\area.txt') as f :
    arealist = f.readlines()
    
arealist = [x.strip() for x in arealist]     
#print(arealist)

k = 0
total=0
for i in range(len(arealist)):
    
    k+=1
    url2="https://www.google.co.in/maps/search/Multispeciality+hospitals+in+"+arealist[i]


    #webbrowser.open(url2)
    

    res2=requests.get(url2)
    Text=res2.text

    #print(Text)

    soup2=bs4.BeautifulSoup(res2.text,'html.parser');
    #span itemprop="address"

    
    obj=re.compile(r'\"Hospital')
    #print(obj.findall(Text))
    elems=obj.findall(Text)
    total+=len(elems)
    #print(total)
    
    #print(len(elem))
    print(arealist[i]+ ' '+ str(len(elems)))
    with open(filename, 'a') as out:
            out.write(str(k) + ' '+str(len(elems))+'\n')

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

    
