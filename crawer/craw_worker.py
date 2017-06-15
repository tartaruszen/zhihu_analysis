from zhihu_topic_api import save_topic_all
import time

import redis
r = redis.StrictRedis(host='redis-pubsub', port=6379, db=0)
p = r.pubsub()
p.subscribe('graph-to-craw', 'text-to-craw')

if __name__ == '__main__':
	while True:
		message = p.get_message()
		if message:
			print message
			if message['channel'] == 'graph-to-craw' and message['type'] == 'message':
				craw = save_topic_all(message['data'])
				if craw:
					r.publish('craw-to-text', 'craw '+message['data']+' success')
			elif message['channel'] == 'text-to-craw' and message['type'] == 'message':
				craw = save_topic_all(message['data'])
				if craw:
					r.publish('craw-to-text', 'craw '+message['data']+' success')
			else:
				pass
		time.sleep(0.001)
	