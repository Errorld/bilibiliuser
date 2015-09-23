#!/usr/bin/env python3
#coding: utf-8
import urllib
import urllib.request
from bs4 import BeautifulSoup

head_url='http://space.bilibili.com/'
UIDS=range(1,15111111)

def grab_html(url):
	#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windos NT)'
	#headers = {'User-Agent': user_agent}	
	req = urllib.request.Request(url)#, headers=headers)
	try:
		response = urllib.request.urlopen(req)
	except urllib.request.URLError as e:
		if hasattr(e, 'code'):
			print('Error code: ',e.code)
			return False
		elif hasattr(e, 'reason'):
			print('Reason: ', e.reason)
			return False
	else:
		data = response.read()
		body = data.decode('utf-8')
		return body
	
def find_name(html):
	soup= BeautifulSoup(html, 'html.parser')
	title= soup.title.get_text()
	return title
for UID in UIDS:
	url=head_url+str(UID)
	print(url)
	html=grab_html(url)
	if html:
		title=find_name(html)
	print(title)
