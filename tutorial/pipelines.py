# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import sqlite3


class TutorialPipeline(object):
	def __init__(self):
		self.file = codecs.open('data_utf8.json', 'w', encoding='utf-8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + "\n"
		self.file.write(line)
		return item

	def close_spider(self, spider):
		self.file.close()
	# def process_item(self, item, spider):
	# 	for field in item:
	# 		print field + ': ' + item[field]


class SqlitePipeline(object):

	def __init__(self):
		self.movie_id = 0;
		self.db = sqlite3.connect("movie.db")
		self.cursor = self.db.cursor()
		self.cursor.execute('create table movie_info (movie_id integer primary key, movie_name text, movie_link text)')

	def process_item(self, item, spider):
		self.cursor.execute("INSERT INTO movie_info(movie_id,movie_name,movie_link) values(?,?,?)",(self.movie_id,item['movie_name'],item['download_link'])) 
		self.movie_id = self.movie_id + 1
		self.db.commit()
		return item

	def close_spider(self, spider):
		self.cursor.close()
		self.db.close()