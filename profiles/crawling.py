import imaplib
import re

import os

proxy = 'http://vivekraj:maymay@172.16.115.46:3128'

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

servers=['teesta','naambor','disang','tamdil','dikrong']

def crawl_print(username,password,search_keyword,server_no,regex,start):
	messages=[]
	try:
		print("trying")
		print(username)
		print(password)
		print(search_keyword)
		print(servers[server_no])
		M = imaplib.IMAP4_SSL(servers[server_no]+'.iitg.ernet.in')
		M.login(username, password)
	except Exception as e:
		print(e)
		return {'end':1000,'messages':messages}
	M.select()
	regex=r""+regex.pattern
	typ, data = M.search(None, 'ALL')
	typ1, data1 = M.search(None, 'UNSEEN')
	for num in data[0].split():
		if int(num)>start:
			typ, data = M.fetch(num, 'BODY[1]')
			try:
				x=data[0][1].decode('cp1252')
				if search_keyword.lower() in x.lower():
					if re.search(regex,x.split("Original Message")[0]):
						messages.append(re.search(regex,x.split("Original Message")[0]).group(0)[1:len(re.search(regex,x.split("Original Message")[0]).group(0))-1])
			except:
				print("error")
	b=num
	for num in data1[0].split():
		M.store(num, '-FLAGS', '\\SEEN')
	M.close()
	M.logout()
	print(b)
	print(messages)
	return {'end':b,'messages':messages}

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib

def get_cse_info(username,path):
	url = "https://www.iitg.ernet.in/cseweb/automation/people?statusCode=3c6234c6f6ff2880ec3c0c979ba87ba4"

	content = urlopen(url).read()

	soup = BeautifulSoup(content,'lxml')

	x=soup.find_all("img")

	flag=0

	for y in x:
		if username in y['src']:
			flag=1
			name=(y["title"])
			urllib.request.urlretrieve("https://www.iitg.ernet.in"+y['src'],'/home/vivek/Projects/memoir/media/'+path+username+".jpeg")

	z=soup.find_all("td")

	for a in z:
		if username in str(a):
			if (len(a.find_all(text=True))>2):
				c=0
				post=a.find_all(text=True)[1]
				for b in a.find_all(text=True):
					c=c+1
					if "phone" in b.lower():
						phone=a.find_all(text=True)[c]

					if "room" in b.lower():
						room=a.find_all(text=True)[c]
	if flag:
		return {'phone':phone,'room':room,'post':post}
	return {}