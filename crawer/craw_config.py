import redis
from pymongo import MongoClient

def wait_for_redis(r):
	ready = True
	while ready:
		try:
			r.set('ready','go')
			ready = False
		except:
			pass
			
rp = redis.StrictRedis(host='localhost', port=6379, db=0)
#rp = redis.StrictRedis(host='redis-pubsub', port=6379, db=0)
wait_for_redis(rp)

def wait_for_mongo(c):
	ready = True
	while ready:
		try:
			c.database_names()
			ready = False
		except:
			pass

client = MongoClient('localhost', 27017)
#client = MongoClient('mongo-crawer', 27017)
wait_for_mongo(client)
db = client.zhihu

def get_config():
	return {'rp':rp,'db':db}