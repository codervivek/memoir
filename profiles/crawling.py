import imaplib
import re

servers=['teesta','naambor','disang','tamdil','dikrong']

def crawl_print(username,password,search_keyword,server_no,regex,start):
	messages=[]
	M = imaplib.IMAP4_SSL(servers[server_no]+'.iitg.ernet.in')
	M.login(username, password)
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

# g=crawl_print('jatingoyal','c7aVpnwA','lecture',4,re.compile('\"(.*?)\"'),1)