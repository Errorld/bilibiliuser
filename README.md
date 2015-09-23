# bilibili用户分析器（1）

标签（空格分隔）： bilibiil 爬虫 Python

---

#1. 来源

B站用户空间的地址是http://space.bilibili.com/UID
根据这个UID应该很容易就把所有用户都遍历一次
新手只想把所有用户名导出，以后可能扩展一下功能，把每个用户的投稿信息数据一起爬出来

- [x] 问题1
- [ ] 问题2

#2. 因为技术难题先转为抓取用户空间名
```
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
```
可以工作到[bilibili.com/9](http://www.bilibili.com/9)这个页面是404，需要学习异常处理

- [x] 问题3

#3. 异常处理解决
```
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
	req = urllib.request.Request(url）#, headers=headers)
	try:
		response = urllib.request.urlopen(req)  #是否异常
	except urllib.request.URLError as e:
		if hasattr(e, 'code'):  #判断是否HTTPError
			print('Error code: ',e.code)    打印错误号
			return False
		elif hasattr(e, 'reason'):  #判断是否URLError
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
```
中午睡了一觉醒来发现它还在跑，~~有点感动~~
![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-23/8631215.jpg)

#4. 总结
- 通过spacename.py项目学习了爬虫的异常处理
- 尝试了用MD写东西

    **spacename.py 完成任务**

    下面要进行：
    1. 文件保存
    2. 字符编码问题
    3. 改进文档结构


#* 问题与解决问题
1. UnicodeEncodeError: ‘gbk’ codec can’t encode character u’\u200e’ in position 43: illegal multibyte sequence
    
- 这个问题是WINDOWS独有的原因可能是CMD和POWERSHELL使用编码为GBK，暂时没时间管。[别人博客里的分析](http://www.crifan.com/unicodeencodeerror_gbk_codec_can_not_encode_character_in_position_illegal_multibyte_sequence/)
- 使用PYTHON 的IDLE也没有这个编码问题
> 工作环境改为linux   开启我的**VMWAREUBUNTU**

2.
抓取html页面后，所有URL返还的都是同一页面
```
<span id="space-owner-name">(´･ω･`)</span>
```


- 可能是需要登录？在浏览器上注销账号后也可以正常获得页面
- 可能是需要模仿浏览器？这个任务先放一下，学习了模拟浏览器后再来
- 然而我眉头一皱，发觉事情并不单纯 ![](http://7xlyu9.com1.z0.glb.clouddn.com/15-9-23/70544866.jpg)
在source里也是这个卖萌货，和element里发现的用户名不同。需要学习JS,HTML,CSS后再回来
- 发现在某一版本更新后B站空间名已经同一为"NAME的空间"
3.目前效果
```
>>> ================================ RESTART ================================
>>> 
http://space.bilibili.com/1
bishi的空间
http://space.bilibili.com/2
碧诗的空间
http://space.bilibili.com/3
囧囧倉的空间
http://space.bilibili.com/4
枢木朱雀的空间
http://space.bilibili.com/5
幻想乡的空间
http://space.bilibili.com/6
腹黑君的空间
http://space.bilibili.com/7
Tzwcard的空间
http://space.bilibili.com/8
无垢肛勤湿的空间
http://space.bilibili.com/9
Traceback (most recent call last):
  File "d:\Documents\GitHub\bilibiliuser\spacename.py", line 30, in <module>
    html=grab_html(url)
  File "d:\Documents\GitHub\bilibiliuser\spacename.py", line 16, in grab_html
    response = urllib.request.urlopen(req)
  File "C:\Python34\lib\urllib\request.py", line 161, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Python34\lib\urllib\request.py", line 469, in open
    response = meth(req, response)
  File "C:\Python34\lib\urllib\request.py", line 579, in http_response
    'http', request, response, code, msg, hdrs)
  File "C:\Python34\lib\urllib\request.py", line 507, in error
    return self._call_chain(*args)
  File "C:\Python34\lib\urllib\request.py", line 441, in _call_chain
    result = func(*args)
  File "C:\Python34\lib\urllib\request.py", line 587, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found
```
遇到404页面
问题通过异常处理解决：
```
>>> ================================ RESTART ================================
>>> 
http://space.bilibili.com/1
bishi的空间
http://space.bilibili.com/2
碧诗的空间
http://space.bilibili.com/3
囧囧倉的空间
http://space.bilibili.com/4
枢木朱雀的空间
http://space.bilibili.com/5
幻想乡的空间
http://space.bilibili.com/6
腹黑君的空间
http://space.bilibili.com/7
Tzwcard的空间
http://space.bilibili.com/8
无垢肛勤湿的空间
http://space.bilibili.com/9
Error code:  404
无垢肛勤湿的空间
http://space.bilibili.com/10
mikumiku没穿内裤的空间
http://space.bilibili.com/11
春哥的空间
http://space.bilibili.com/12
Error code:  404
```
