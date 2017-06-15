import redis
rt = redis.StrictRedis(host='redis-pubsub', port=6379, db=0)

from pymongo import MongoClient

client = MongoClient('mongo-crawer', 27017)
db = client.zhihu
topic = db.topic
question = db.question
question_answer = db.question_answer
answer_comment = db.answer_comment
answer = db.answer
comment = db.comment
member = db.member

def load_text(topic_token):
	return True