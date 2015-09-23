#!usr\bin\env python3
#coding: utf-8
import urllib
import urllib.request
import tornado.httpclient
from bs4 import BeautifulSoup

head_url='http://space.bilibili.com/'
UIDS=range(1,15111111)

def grab_html(url):
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windos NT)'
	#urllib.request.urlencode(user_agent)
	headers = {'User-Agent': user_agent}	
	req = urllib.request.Request(url, headers=headers)
	response = urllib.request.urlopen(req)
	print(response)
	data = response.read()
	body = data.decode('utf-8')
	return body
	print(body)
def find_name(html):
	soup= BeautifulSoup(html, 'html.parser')
	name= soup.find(id='space-owner-name').get_text()
	print(name)
	return name
for UID in UIDS:
	url=head_url+str(UID)
	print(url)
	print(UID)
	html=grab_html(url)
	name=find_name(html)
	print(name)

#url = head_url+str(1)	
#html=grab_html(url)
#print(html)
