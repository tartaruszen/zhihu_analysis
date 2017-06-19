import time
import requests

import socket

def get_my_ip():
	"""
	Returns the actual ip of the local machine.
	This code figures out what source address would be used if some traffic
	were to be sent out to some well known address on the Internet. In this
	case, a Google DNS server is used, but the specific address does not
	matter much.  No traffic is actually sent.
	"""
	try:
		csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		csock.connect(('8.8.8.8', 80))
		(addr, port) = csock.getsockname()
		csock.close()
		return addr
	except socket.error:
		return "127.0.0.1"

def get_host_ip():
	ip =  get_my_ip()
	ipl = ip.split('.')
	ipl[-1] = '1'
	return '.'.join(ipl)

def init_api():
	host_ip = get_host_ip()
	#ensure kong admin start!
	kong = False
	while kong == False:
		try:
			r = requests.get('http://{}:8001'.format(host_ip))
			j = r.json()
			kong = True
		except:
			print 'wait for kong!'
			time.sleep(3)
	# add api api-text
	url = 'http://{}:8001/apis/'.format(host_ip)
	data = {
		'name':'api-text',\
		'upstream_url':'http://text:5000'
	}
	r = requests.post(url,data=data)
	# add key-auth to keyword
	url = 'http://{}:8001/apis/api-text/plugins/'.format(host_ip)
	data = {'name':'key-auth'}
	r = requests.post(url,data=data)
	# add consumers
	url = 'http://{}:8001/consumers/'.format(host_ip)
	data = {'username':'comsumer-text'}
	r = requests.post(url,data=data)
	# set comsumer-text key
	url = 'http://{}:8001/consumers/comsumer-text/key-auth'.format(host_ip)
	data = {'key':'key-text'}
	r = requests.post(url,data=data)
	print 'api init sucess!'

if __name__ == '__main__':
	init_api()