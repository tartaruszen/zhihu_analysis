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
			
rp = redis.StrictRedis(host='redis-pubsub', port=6379, db=0)
wait_for_redis(rp)

def wait_for_mongo(db):
	ready = True
	while ready:
		try:
			db.add_user('zhihu')
			ready = False
		except:
			pass
			
client = MongoClient('mongo-crawer', 27017)
db = client.zhihu
wait_for_mongo(db)

def get_config():
	return {'rp':rp,'db':db}