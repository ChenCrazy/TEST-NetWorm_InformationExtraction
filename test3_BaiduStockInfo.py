# 功能描述:
# 目标：获取上交所和深交所所有股票的名称和交易信息
# 输出：保存到文件
# 技术路线：requests-bs4-re
#候选数据网站的选择：新浪股票、百度股票
#	选取原则：股票信息静态存在于HTML页面中，非js代码生成，没有Robots协议限制
#	选取方法：浏览器F12，查看源代码确认
#	选取心态：不要纠结于某个网站，多找信息源尝试——>东方财富网
# 步骤：
# 1.从东方财富网获取股票列表
# 2.根据股票列表逐个到百度股票获取个股信息
# 3.将结果存储到文件中
import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
#获得URL对应的页面
	try:
		r = requests.get(url, time = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def getStockList(lst, stockURL):
#获得股票的信息列表
	html = getHTMLText(stockURL)
	soup = BeautifulSoup(html, 'html.parser')
	a = soup.find_all('a')
	for i in a:
		try:
			href = i.attrs['href']
			lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
		except:
			continue

def getStockInfo(lst, stockURL, fpath):
#获得每支个股的信息，并将其存到一个数据结构，包括三个参数：保存所有股票的信息列表，获得信息的网站，以及将要信息存储文件的路径
	for stock in lst:
		url = stockURL + stock + ".html"
		html = getHTMLText(url)
		try:
			if html=="":
				continue
			infoDict = {}
			soup = BeautifulSoup(html,'html.parser')
			stockInfo = soup.find('div',attrs = {'class':'best-name'})[0]
			infoDict.update({'股票名称': name.text.split()[0]})

			keyList = stockInfo.find_all('dt')
			valueList = stockInfo.find_all('dd')
			for i in range(len(keyList)):
				key = keyList[i].text
				val = valueList[i].text
				infoDict[key] = val
			
			with open(fpath, 'a', encoding='utf-8') as f:
				f.write( str(infoDict) + '\n')
		except:
			traceback.print_exc()
			continue

def main():
	#获得股票列表的链接
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
	#获取股票信息的链接的主体部分
	stock_info_url = 'https://gupiao.baidu.com/stock/'
	#输出文件保存位置
	output_file = 'D:/BaiduStockInfo.txt'
	slist = []
	getStockList(slist, stock_list_url)
	getStockInfo(slist, stock_info_url, output_file)

main()