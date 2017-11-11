import getpass, imaplib

M = imaplib.IMAP4_SSL('dikrong.iitg.ernet.in')
M.login('vivekraj', 'ZQMVzYzT')
M.select()
typ, data = M.search(None, 'ALL')
flag=0
flag1=0
str=""
a=1
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print("\nMessage ", a)
    # for word in data[0][1].split():
    word=data[0][1]
    x=word.decode('cp1252')
    # if "Importance" in x:
    #     flag=1
    #     print("xyz")
    # elif flag==1:
    # 	if "Content-Type" in word.decode('cp1252'):
    #         # if not "Content-Type: text/plain" in word.decode('cp1252'):
    #         break
    # 	else :
    # 		str = str + " " + word.decode('cp1252')
    z=x.split("Content-Type:",1)
    for y in z:
        if not (len(y)>20000):
            print(y)
    # print x.split("Content-Type: text/plain",1)[0] 
    # print(str)
    for word in data[0][1].split():
    	x=word.decode('cp1252')
    	if "Importance" in x:
    		flag=1
    	elif flag==1:
    		if "Content-Type" in word.decode('cp1252'):
    			break 
    		else :
    			str = str + " " + word.decode('cp1252')
    a=a+1
    print(str)
    str=""
    flag=0
    flag1=0

    # print ('Message : %s\n%s\n' % (num, data[0][1]))

M.close()
M.logout()
