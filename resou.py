import requests
from bs4 import BeautifulSoup
import time
import csv

url = 'https://s.weibo.com/top/summary'
web_data = requests.get(url).content.decode('utf-8')
soup = BeautifulSoup(web_data, 'lxml')
tbody = soup.find(name='tbody')
tr_list = tbody.find_all(name='tr')

resou_lists = []
localtime = time.asctime( time.localtime(time.time()) )
for item in tr_list:
	if item.find(attrs={'class': 'td-01 ranktop'}):
		num = item.find(attrs={'class': 'td-01 ranktop'}).get_text()
	else:
		num = 'top'
	keyword = item.find(attrs={'class': 'td-02'}).a.get_text()
	if item.find(attrs={'class': 'td-02'}).span:
		hot = item.find(attrs={'class': 'td-02'}).span.get_text()
	else:
		hot = ''
	if item.find(attrs={'class': 'td-03'}).i:
		charac = item.find(attrs={'class': 'td-03'}).i.get_text()
	else:
		charac = ' '
	resou_item = {
		'time': localtime,
		'number': num,
		'keyword': keyword,
		'hot': hot,
		'character': charac
	}
	resou_lists.append(resou_item)

headers = ['time', 'number', 'keyword', 'hot', 'character']
with open('resou.csv', 'a') as f:
    f_csv = csv.DictWriter(f, headers)
    # f_csv.writeheader()
    f_csv.writerows(resou_lists)
