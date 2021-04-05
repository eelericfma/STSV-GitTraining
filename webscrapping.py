from flask import Flask, render_template
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver 

driver= webdriver.Chrome(executable_path="C:\python3.9.2\python_projects\chromedriver.exe")
driver.get('https://www.espncricinfo.com/')
content = driver.page_source # page source of web page we opened via driver 
driver.quit() 

results=[] #empty list for storing variables 
soup = BeautifulSoup(content, features="html.parser") # to clear large mess of content


#begining extracting data from parsed soup into results list 
for element in soup.findAll(attrs={'class': 'story-title'}): # closest possible parent of target element 
	name= element.find('span') #finding tag which is child of above 
	if name.text not in results: # name must exists else error is thrown 
		results.append(name.text)

print('Results are: ')
print (results)

#saving data frame to CSV

df= pd.DataFrame({'Names':results})
df.to_csv('names.csv', index=False, encoding='utf-8')


app= Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__== '__main__':
    app.run(debug=True)    