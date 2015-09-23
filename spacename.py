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
	#print(response)
	data = response.read()
	body = data.decode('utf-8')
	return body
	
def find_name(html):
	soup= BeautifulSoup(html, 'html.parser')
	title= soup.title.get_text()
	#print(title)
	return title
for UID in UIDS:
	url=head_url+str(UID)
	print(url)
	html=grab_html(url)
	title=find_name(html)
	print(title)

#url = head_url+str(1)	
#html=grab_html(url)
#print(html)
