import requests
from bs4 import BeautifulSoup
import time

url = 'https://s.weibo.com/top/summary'
web_data = requests.get(url).content
soup = BeautifulSoup(web_data, 'lxml')
tbody = soup.find(name='tbody')
tr_list = tbody.find_all(name='tr')

t_title = soup.find('title').text
print(t_title)

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

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
		type = item.find(attrs={'class': 'td-03'}).i.get_text()
	else:
		type = ' '
	print('序号：' + num)
	print('关键词：' + keyword)
	print('热度：' + hot)
	print('特征：' + type)
	print('********************')
