import time
import requests

def init_api():
	#ensure kong admin start!
	kong = False
	while kong == False:
		try:
			r = requests.get('http://localhost:8001')
			j = r.json()
			kong = True
		except:
			print 'wait for kong!'
			time.sleep(3)
	# add api api-text
	url = 'http://localhost:8001/apis/'
	data = {
		'name':'api-text',\
		'upstream_url':'http://text:5000'
	}
	r = requests.post(url,data=data)
	# add key-auth to keyword
	url = 'http://localhost:8001/apis/api-text/plugins/'
	data = {'name':'key-auth'}
	r = requests.post(url,data=data)
	# add consumers
	url = 'http://localhost:8001/consumers/'
	data = {'username':'comsumer-text'}
	r = requests.post(url,data=data)
	# set comsumer-text key
	url = 'http://localhost:8001/consumers/comsumer-text/key-auth'
	data = {'key':'key-text'}
	r = requests.post(url,data=data)
	print 'api init sucess!'

if __name__ == '__main__':
	init_api()