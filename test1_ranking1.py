# 通过上海交通大学最好大学网获取排名
# 功能描述：
# 输入：大学排名URL链接
# 输出：大学排名信息的屏幕输出（排名，大学名称，总分）
# 技术路线：requests-bs4
# 定向爬虫：仅对输入URL（指定的）进行爬取，不扩展爬取。
# 步骤：
# 1.从网络上获取大学排名网页内容 getHTMLText()
# 2.提取网页内容中信息到合适的数据结构 fillUnivList()
# 3.利用数据结构展示并输出列表结果 printUnivList()
import requests
from bs4 import BeautifulSoup
import bs4

def  getHTMLText(url):
	#输入需要获取的url信息，输出url的内容
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return " "

def fillUnivList(ulist, html):
	#将一个页面放到list列表ulist中
	soup = BeautifulSoup(html, "html.parser")
	for tr in soup.find('tbody').children:
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist,num):
	#对中文打印格式进行优化

	tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
	#将ulist中的信息格式化输出，num表示希望打印出的选项元素数目
	print(tplt.format("排名","学校排名","总分",chr(12288)))
	for i in range(num):
		u = ulist[i]
		print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
	uinfo = []
	url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
	html = getHTMLText(url)
	fillUnivList(uinfo, html)
	printUnivList(uinfo, 20)  #排名20  
main()


