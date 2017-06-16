import time
from text_etl import load_text
from text_analysis import extract_keyword

import redis
r = redis.StrictRedis(host='redis-pubsub', port=6379, db=0)
p = r.pubsub()
p.subscribe('craw-to-text')

rt = redis.StrictRedis(host='redis-text', port=6380, db=0)

if __name__ == '__main__':
	while True:
		message = p.get_message()
		if message:
			print message
			if message['channel'] == 'craw-to-text' and message['type'] == 'message':
				if message['data'].endswith('success'):
					topic_token = message['data'].split(' ')[1]
					if not rt.exists('corpora'+topic_token):
						load_text(topic_token)
					text = tr.get('corpora'+topic_token)
					keywords = extract_keyword(text)
					for k,v in keywords.items():
						rt.lpush('keyword'+topic_token,str(k)+':'+str(v))
			else:
				pass
		time.sleep(0.001)
