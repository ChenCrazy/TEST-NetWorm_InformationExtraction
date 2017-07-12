# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaidustocksPipeline(object):
    def process_item(self, item, spider):
        return item
class BaidustocksInfoPipeline(object):
	#open_spider指的是当一个爬虫被调用时，对应的piplines启动的方法
	def open_spider(self, spider):
		self.f = open('BaiduStockInfo.txt','w')
	#close_spider指的是当一个爬虫被关闭时，对应的piplines关闭的方法
	def close_spider(self,spider):
			self.f.close()	
	#process_item指的是对每一个item项进行处理时，piplines对应的方法		
	def process_item(self, item,spider):
		#将获得的股票字典信息写到一个文件
		try:
			line = str(dict(item)) + '\n'
			self.f.write(line)
		except:
			pass
		return item
	