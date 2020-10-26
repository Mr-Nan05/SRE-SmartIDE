import requests
from bs4 import BeautifulSoup

cookie ='prov=548bf8e0-bbd3-2f92-f314-145d3888f3e6; __qca=P0-1324908065-1593929000356; _ga=GA1.2.172973307.1594087955; usr=p=%5b160%7c%3bNewest%3b%5d%5b10%7c15%5d; _gid=GA1.2.802337396.1603621559; acct=t=Q5GQngGeMLAu0E%2f0z8b2dV8tNjbosC7c&s=FNQORcM%2fJ5%2bo9ZKIAfzaFHl3zSOUlmlB; _gat=1'
headers = {
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
,'Cookie' : cookie
}

res = requests.get('https://stackoverflow.com/questions/tagged/ide?tab=newest&page=2&pagesize=15', headers = headers)
soup = BeautifulSoup(res.text)
items = soup.select('div>h3>a')
for item in items:
    print(item['href'])