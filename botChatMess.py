from fbchat import Client
from fbchat.models import *

import time


timestampPerMinute = 61500

email = "48e83cca@blurme.net"
passw = "HƠ122333}"

partnerID = "100005128032970"
hienID = "100005935830246"
aichoaiID = "100023348531077"


aichoaiSessionCookies = {'sb': 'xCL3XIapCuUTloNItzGlBUwD', 'spin': 'r.1000787156_b.trunk_t.1559700171_s.1_v.2_', 'datr': 'xCL3XCiKt6ofkcf6KaVtpNFV', 'c_user': '100023348531077', 'fr': '1JPYVUgHAVkf3EuFL.AWVV7pgNIyDeEwxzfsxuSO_bqvQ.Bc9yLE.79.AAA.0.0.Bc9yLE.AWUMZk7T', 'noscript': '1', 'xs': '24%3Acd0ahrzwjaHf3A%3A2%3A1559700165%3A13346%3A13373'}
# MainSessionCookies = {'datr':'2p3vW_me5vWqFuyUM4K5-5wi', 'sb':'D57vWxA5EnjB9-lXsY8aWKQi', 'c_user':'100005128032970', 'xs':'3%3A22xIYiTz1NBK3w%3A2%3A1556350235%3A5717%3A6340', 'spin':'r.1000784160_b.trunk_t.1559637403_s.1_v.2_', 'dpr':'1.25', 'act':'1559700339545%2F16', 'fr':'1xFC3r9aRdOyY8Pav.AWX5GCF3reMqsajn51iZMxY4JSc.Bb753a.Hp.Fzx.0.0.Bc9yN1.AWW7lmTt', 'presence':'EDvF3EtimeF1559700347EuserFA21B05128032970A2EstateFDt3F_5b_5dG559700347761CEchFDp_5f1B05128032970F2CC', 'wd':'898x722}
MainSessionCookies = {'sb': 'D57vWxA5EnjB9-lXsY8aWKQi', 'spin': 'r.1000784160_b.trunk_t.1559637403_s.1_v.2_', 'datr': '2p3vW_me5vWqFuyUM4K5-5wi', 'c_user': '100005128032970', 'fr': '1xFC3r9aRdOyY8Pav.AWX5GCF3reMqsajn51iZMxY4JSc.Bb753a.Hp.Fzx.0.0.Bc9yN1.AWW7lmTt', 'noscript': '1', 'xs': '3%3A22xIYiTz1NBK3w%3A2%3A1556350235%3A5717%3A6340'}

# client = Client(email, passw)

# print('Own id: {}'.format(client.uid))

# client.sendMessage('Hi me part2!', thread_id = client.uid, thread_type = ThreadType.USER)

# client.logout()
# 

def printMess(message):
	print("----------{}----------".format(message.uid))
	print("\"{}\"\nauthor: {}___time: {}___is_read: {}\n".format(
		message.text, message.author, message.timestamp, message.is_read))

def timestampToInt(timestamp):
    import time
    d,b,y,h,m,s = time.strftime("%d:%b:%Y:%H:%M:%S", time.gmtime(timestamp)).split(':')
    return d, b, y, h, m, s

class repMess():

	HienID = "100005935830246"
	NTHID = "100005128032970"
	AiChoAiID = "100023348531077"
	NgayTroiVePhiaCuID = "100011428687864"
	HuyenID = "100008446578529"
	ChiConNhungMuaNhoID = "100011345565501"
	YenNhiID = "100008455412548"

	eny = [HienID, NgayTroiVePhiaCuID]
	test = [AiChoAiID, NTHID, ChiConNhungMuaNhoID]
	bff = [HuyenID, YenNhiID]

	textRep = {
		"eny" : ["Chị Hiền. Anh Hà hiện đang không online. Nếu gấp thì chị vui lòng call nhé. \nChúc chị vui vẻ!",
				 "Anh Hà yêu chị Hiền, nhưng anh Hà đang ko onl",
				 "Hà hiện đang không online. hi",
				 "I Love U"],
		"bff" : "Hà hiện đang không online. hi",
		"test" : "Bạn Hà hiện đang không online. \nTin nhắn được gửi tự động, vui lòng không trả lời"
	}

	def __init__(sefl):
		return 1

class EchoBot(Client):
	def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
		self.markAsDelivered(author_id, thread_id)
		self.markAsRead(author_id)

		# if author_id in [hienID, aichoaiID]:
		# 	self.sendMessage(waitingMessageForHien, thread_id=thread_id, thread_type = thread_type)


# client.setSession(MainSessionCookies)

# print(client.getSession())

def fetchAllMessages_Of_1_ID(client, thread_id):
	import time
	maxOfNumMess = 15000
	countFetch = 0

	threadMessages = client.fetchThreadMessages(thread_id = thread_id, limit = maxOfNumMess)

	while (len(threadMessages) == maxOfNumMess):
		
		print('Sleep')
		time.sleep(1)

		countFetch += 1
		t1 = threadMessages[maxOfNumMess-1].timestamp
		print(t1)

		threadMessages = client.fetchThreadMessages(thread_id = thread_id, limit = maxOfNumMess, before = t1)

		print('len: ', len(threadMessages))
		print(threadMessages[0].text)

		print(countFetch*(maxOfNumMess-1) + len(threadMessages))
		print("-------------------------")

	return countFetch*(maxOfNumMess-1) + len(threadMessages)

def statisticalMessage(client):
	lastThreads = client.fetchThreadList()
	for thread in lastThreads:
		if thread.type == ThreadType.USER:
			print("{} {}".format(thread.name, thread.message_count))

# print(fetchAllMessages_Of_1_ID(client, hienID))

def statisticalWordInMessages(client, thread_id):
	threadMessages = client.fetchThreadMessages(thread_id = thread_id, limit = maxOfNumMess)

def checkLastMessages(client, limit=5, maxOfNumLastMess = 20, minMinutes = 2, maxMinutes = 5):
	lastThreads = client.fetchThreadList(limit = limit)

	print("_________________ list last Threads _________________")
	for thread in lastThreads:
		print(thread.name)
	print("_____________________________________________________")

	# repMessage(client, thread)
	for thread in lastThreads:
		print(thread.name)
		if isNewFriendMessage(client, thread, boundary_Mesage_Count = 60, minMinutes=minMinutes, maxMinutes=maxMinutes):
			print("isNewFriendMessage")
			# client.sendMessage("test tin nhắn đợi", thread_id = thread.uid)
			repMessage(client, thread.uid)
	return 0

def isNewFriendMessage(client, thread, maxOfNumLastMess = 20, boundary_Mesage_Count = 3000, minMinutes = 5, maxMinutes = 10):
	# print("type: ", thread.type, thread.type != ThreadType.USER)
	if (thread.type != ThreadType.USER):
		return False
	if (thread.is_friend == False):
		return False
	
	# if (thread.message_count < boundary_Mesage_Count):
	# 	return False
	lastMessages = client.fetchThreadMessages(thread.uid, limit = maxOfNumLastMess)[0]
	# print("now: ", time.time())
	printMess(lastMessages)
	if (lastMessages.author == client.uid):
		return False
	
	timestamp = int(lastMessages.timestamp)/1000

	if not timeInMinMaxMinutes(timestamp, minMinutes, maxMinutes):
		return False
	

	return not lastMessages.is_read

def timeInMinMaxMinutes(timestamp, minMinutes=2, maxMinutes=5):
    import time
    d, b, y, h, m, s = timestampToInt(timestamp)
    nowD, nowB, nowY, nowH, nowM, nowS = timestampToInt(time.time())
    print(d, b, y, h, m, s)
    print(nowD, nowB, nowY, nowH, nowM, nowS )
    if (d+b+y == nowD+nowB+nowY):
        minutes =(60*int(nowH)+int(nowM)+float(nowS)/60 - 60*int(h) - int(m) - float(s)/60)
        print("{} <= {} <= {}   {}".format(minMinutes, minutes, maxMinutes, (minMinutes <= minutes <= maxMinutes)))

        return (minMinutes <= minutes <= maxMinutes)
    return False

def repMessage(client, thread_id):
	text = ""
	# print(thread_id)
	if (thread_id in repMess.eny):
		import random

		text = random.choice(repMess.textRep['eny'])

	elif (thread_id in repMess.bff):
		text = repMess.textRep['bff']

	elif (thread_id in repMess.test):
		text = repMess.textRep['test']


	if (text!=""):
		client.sendMessage(text, thread_id)
		print("rep ", text)
	# print(client.fetchThreadMessages(thread.uid, limit = 1)[0].author)

	return 0


client = Client("", "", session_cookies = MainSessionCookies)

for i in range(1,10):
	print("-----------------------------Check {}-----------------------------".format(i))
	checkLastMessages(client, minMinutes = 1, maxMinutes = 5)
	time.sleep(15)


'''
import time

ts1 = time.time()
time.sleep(1)
ts2 = time.time()
time.sleep(2)
ts3 = time.time()

print(ts1)
print(ts2)
print(ts3)




# messages = client.fetchThreadMessages(thread_id = hienID, limit = 15000, before = 1521299787912)
# print(len(messages))

# threadList = client.fetchThreadList(limit = 5)

print(threadList[1])
gr = threadList[0]
x = threadList[2]

print(x.type)
print(type(x))
# print(isinstance(x, fbchat._user.User))
print(type(gr))
print(x.type == ThreadType.USER)
# print(threadList[4])

# client.listen()
# client.logout()

1559877226
1559876774077
'''