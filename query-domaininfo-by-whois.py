#!/usr/bin/env python3 
#-*- coding: utf-8 -*-

#首先我们要导入requests模块和bs4模块里的BeautifulSoup和time模块
import requests
import time
from bs4 import BeautifulSoup

#设置好开始时间点
strat=time.time()

class G:
    rb1=None
    rb2=None
    rb3=None
def chax():
    #询问用户要查询的域名
    lid=input('请输入你要查询的域名:')
    #设置浏览器头过反爬
    head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    #设置好url
    url="http://site.ip138.com/{}/".format(lid)
    urldomain="http://site.ip138.com/{}/domain.htm".format(lid)
    url2="http://site.ip138.com/{}/beian.htm".format(lid)
    url3="http://site.ip138.com/{}/whois.htm".format(lid)
    #打开网页
    rb=requests.get(url,headers=head)
    G.rb1=requests.get(urldomain,headers=head)
    G.rb2=requests.get(url2,headers=head)
    G.rb3=requests.get(url3,headers=head)
    #获取内容并用html的方式返回
    gf=BeautifulSoup(rb.content,'html.parser')
    print('[+]IP解析记录')
    #读取内容里的p标签
    for x in gf.find_all('p'):
      #使用text的内容返回
      link=x.get_text()
      print(link)

chax()


gf1=BeautifulSoup(G.rb1.content,'html.parser')
print('[+]子域名查询')
for v in gf1.find_all('p'):
  link2=v.get_text()
  print(link2)
gf2=BeautifulSoup(G.rb2.content,'html.parser')
print('[+]备案查询')
for s  in gf2.find_all('p'):
  link3=s.get_text()
  print(link3)
gf3=BeautifulSoup(G.rb3.content,'html.parser')
print('[+]whois查询')
for k in gf3.find_all('p'):
  link4=k.get_text()
  print(link4)
end=time.time()
print('查询耗时:',end-strat)
