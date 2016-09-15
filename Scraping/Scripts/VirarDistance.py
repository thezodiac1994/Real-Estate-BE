import requests
import bs4
from bs4 import BeautifulSoup
import urllib2 
import string 
from requests import get
import re

url = "http://www.99acres.com/property-rates-and-price-trends-in-mumbai"
filename = "VirarDistance.txt"
headers = { 'User-Agent' : 'Mozilla/5.0' }

def open_url(url):
    return requests.get(url).text  # returns html

def get_bsoup_object(html):
    return BeautifulSoup(html, "html.parser")  # returns soup (BeautifulSoup's




req = urllib2.Request(url, None, headers)
html = urllib2.urlopen(req).read()
soup = get_bsoup_object(html)
k = 0


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
    print(area_name)

    k+=1

    #url2,soup2 -> google map
    #url2="https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q="+area_name+"%20to%20airport"
    url2="https://www.google.com/maps/dir/"+area_name+"/Virar"
    #print(url2)
    #req2 = urllib2.Request(url2, None, headers)
    #html2 = urllib2.urlopen(req2).read()
    #soup2 = get_bsoup_object(html2)
    res2=requests.get(url2)
    Text=res2.text
    
    #soup2=bs4.BeautifulSoup(res2.text,'html.parser')
    #dist=soup2.find('div',attrs={'jstcache':'413'})

    try:
        #Using re,  find (space)km in text
        obj=re.compile(r'(\]\]\]\],\[\[\[null,\[(\d*),\"((\d)*(\.)*(\d)*) km)')
        Match_object=obj.search(Text)
        dist=Match_object.group(3) #first occurrence
        print(dist)
        print(Match_object.group(1))
        #print(obj.findall(Text))

        with open(filename, 'a') as out:
            out.write(str(k) + ' ' + dist  +'\n')
    
    except:
        with open(filename, 'a') as out:
            out.write(str(k)+ ' '+ '0'+'\n')
        

    

