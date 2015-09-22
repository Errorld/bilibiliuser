#!usr\bin\env python3
#coding: utf-8

import tornado.httpclient
from bs4 import BeautifulSoup

head_url='http://space.bilibili.com/'
UIDS=range(1,15111111)

def grab_html(url):
	cli = tornado.httpclient.HTTPClient()
	data = cli.fetch(url)
	body = data.body.decode('utf-8')
	return body
#	print(body)
def find_name(html):
	soup= BeautifulSoup(html, 'html.parser')
	name= soup.find(id='space-owner-name').get_text()
	print(name)
	return name
for UID in UIDS:
	url=head_url+str(UID)
	print(UID)
	html=grab_html(url)
	name=find_name(html)
	print(name)
	
#url = head_url+str(1)	
#html=grab_html(url)
#print(html)
