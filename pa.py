#!usr/bin/env python3
#coding: utf-8

import tornado.httpclient
from bs4 import BeautifulSoup

head_url='http://space.bilibili.com/'
UIDS=range(1,15111111)

def grab_html(url):
	cli = tornado.httpclient.HTTPClient()
	data = cli.fetch(url)
	body = data.body.decode('utf-8')
	print(body)
def find_name():
	pass

for UID in UIDS:
	url=head_url+str(UID)
	print(url)
	print(UID)
	html=grab_html(url)
#	name=find_name(html)
#	print(name)
	
	
