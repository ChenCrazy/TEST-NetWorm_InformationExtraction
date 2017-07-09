#实战2：淘宝商品比价定向爬虫
#目标：熟练掌握正则表达式在信息提取方面的应用
import requests  #导入requests库 正则库
import re

def getHTMLText(url):
	#getHTMLText函数访问读取页面，经过转码显示文本
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def parsePage(ilt,html):
	#对获取页面源代码研究得到特定键值对名称，使用正则进行匹配
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			ilt.append([price,title])
	except:
		print("")

def printGoodsList(ilt):
	#将匹配结果按照简单格式打印
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("序号","价格","商品名称"))
	count = 0
	for g in ilt:
		count = count + 1
		print(tplt.format(count,g[0],g[1]))

def main():
	goods = '书包'
	depth = 2
	start_url = 'https://s.taobao.com/search?q='+goods
	infoList = []
	for i in range(depth):
		try:
			url = start_url + '&s' + str(44*i)
			html = getHTMLText(url)
			parsePage(infoList, html)
		except:
			continue
	printGoodsList(infoList)

main()