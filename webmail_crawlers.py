import poplib
from email import parser

pop_conn = poplib.POP3_SSL('dikrong.iitg.ernet.in')
pop_conn.user('vivekraj')
pop_conn.pass_('ZQMVzYzT')
# print pop_conn.list()
#Get messages from server:
# messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
str=""
arr=[]
for j in range(len(pop_conn.list()[1])):
	flag=0
	for i in pop_conn.retr(j+1)[1]:
		if flag==1:
			x=i.decode('cp1252')
			if "Content-Type:" in x:
				break
			str=str+"\n"+i.decode('cp1252')
		else:
			if "Importance" in i.decode('cp1252'):
				flag=1

	arr.append(str)
	str=""

a=1
for xyz in arr:
	print("Mail no. :",a)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print(xyz)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	a=a+1
# print(pop_conn.retr(1)[1][2].decode('utf-8'))
# Concat message pieces:
#messages = ["\n".join(mssg[1]) for mssg in messages]
#Parse message intom an email object:
#messages = [parser.Parser().parsestr(mssg) for mssg in messages]
#json_xyz = json.loads(messages)
#print json.dumps(messages, indent=4)
#for message in messages:
#    if "jatingoyal" in message["From"]:
#        print(message)
	
pop_conn.quit()
