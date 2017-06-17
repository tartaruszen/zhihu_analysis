import os
import time
import redis
from pymongo import MongoClient

def wait_for_redis(r):
	ready = True
	while ready:
		try:
			r.set('ready','go')
			ready = False
		except:
			time.sleep(1)
			print 'wait_for_redis!'

def wait_for_mongo(c):
	ready = True
	while ready:
		try:
			c.database_names()
			ready = False
		except:
			time.sleep(1)
			print 'wait_for_mongo!'

if os.name == 'nt':
	rp = redis.StrictRedis(host='localhost', port=6379, db=0)
	client = MongoClient('localhost', 27017)
else:
	rp = redis.StrictRedis(host='redis-pubsub', port=6379, db=0)
	client = MongoClient('mongo-crawer', 27017)
wait_for_redis(rp)
wait_for_mongo(client)
db = client.zhihu

def get_config():
	return {'rp':rp,'db':db}