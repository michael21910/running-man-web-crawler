import requests
from bs4 import BeautifulSoup

html = requests.get('https://newsofcar.net/running-man/all.html')
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text, 'lxml')

# get the days
table_div = sp.find('div', 'items')
days = table_div.find_all('a')
ep = []
for day in days:
    ep.append(int(day.text.strip('Running Man ')))
    
# user inputs
string = int(input('Which running man episode do you want to see?\nThe format is: YYYYmmdd\n'))

# run for loop to find the nearest day
print('This is the nearest episode that you are looking for!')
print('https://newsofcar.net/running-man/' + str(min(ep, key = lambda x:abs(x - string))) + '.html')