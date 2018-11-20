# -*- coding: utf-8 -*-
#@author  :lrl
#@date  :2018-11-20


from minicms.wsgi import *
from news.models import Column,Article

def main():
	columns_url = [
		('sport_news','sports'),
		('social_news','social'),
		('sicence_news','science'),
	]
	for column_name, url in columns_url:
		c = Column.objects.get_or_create(name=column_name,slug=url)[0]
		for i in range(1,11):
			article = Article.objects.get_or_create(
				title='{}_{}'.format(column_name,i),
				slug='article_{}'.format(i),
				content='News_content:  {}  {}'.format(column_name,i)
			)[0]
			article.column.add(c)

if __name__ == '__main__':
	main()
	print("lrl is god ,he Done everything!!!")

