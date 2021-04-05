import requests
from bs4 import BeautifulSoup
url = "https://www.mrs-electronic.com/en/products/relays"
#get the html
r = requests.get(url , verify=False)
htmlContent = r.content
#print(htmlContent)
#Parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)
#html tree traversal
#common use type of objects
#print(type(title)) #tags
#print(type(title.string)) #navigable string
#print(type(soup)) #beautiful soup
#comment
markup ="<p><!--this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)
print(soup2.p.string)
print(type(soup2.p.string))
#exit()
#Get the title of html
title = soup.title
print(title)
#find all paragraph of the page
paras = soup.find_all('p')
print(paras)
#find all achor tags from the page
achors = soup.find_all('a')
#all_links = set() #empty set
print(achors)
#get all the links on the page
#for link in achors:
    #print(link.get('href'))
#    if(link.get('href') != '#'):
#     linkText = "https://www.mrs-electronic.com" +link.get('href')
#      all_links.add(link)
#       print(linkText) 
#find first element paragraph of the page
print(soup.find('p')) 
#find first element of paragraph of the class of page
#print(soup.find('p')['class'])
#find all the elements  with class name
#print(soup.find_all("div", class_="page"))
#get a text from tags/soups
print(soup.find('p').get_text()) 