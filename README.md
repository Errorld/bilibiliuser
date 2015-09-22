# bilibili用户分析器

标签（空格分隔）： 未分类

---

#1. 来源

B站用户空间的地址是http://space.bilibili.com/UID
根据这个UID应该很容易就把所有用户都遍历一次
新手只想把所有用户名导出，以后可能扩展一下功能，把每个用户的投稿信息数据一起爬出来

#2. 

#- 问题与解决问题
    UnicodeEncodeError: ‘gbk’ codec can’t encode character u’\u200e’ in position 43: illegal multibyte sequence
    
- 这个问题是WINDOWS独有的原因可能是CMD和POWERSHELL使用编码为GBK，暂时没时间管。[别人博客里的分析](http://www.crifan.com/unicodeencodeerror_gbk_codec_can_not_encode_character_in_position_illegal_multibyte_sequence/)
- 使用PYTHON 的IDLE也没有这个编码问题
> 工作环境改为linux   开启我的**VMWAREUBUNTU**

```
抓取html页面后，所有URL返还的都是同一页面
<span id="space-owner-name">(´･ω･`)</span>
```


- 可能是需要登录？在浏览器上注销账号后也可以正常获得页面
- 可能是需要模仿浏览器？这个任务先放一下，学习了模拟浏览器后再来