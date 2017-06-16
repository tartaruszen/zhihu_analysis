from zhihu_topic_api import save_topic_all
import time

from text_config import get_config
config = get_config()
rp = config['rp']
rpp = rp.pubsub()
rpp.subscribe('graph-to-craw', 'text-to-craw')

if __name__ == '__main__':
	while True:
		message = rpp.get_message()
		if message:
			print message
			if message['channel'] == 'graph-to-craw' and message['type'] == 'message':
				craw = save_topic_all(message['data'])
				if craw:
					rp.publish('craw-to-text', 'craw '+message['data']+' success')
			elif message['channel'] == 'text-to-craw' and message['type'] == 'message':
				craw = save_topic_all(message['data'])
				if craw:
					rp.publish('craw-to-text', 'craw '+message['data']+' success')
			else:
				pass
		time.sleep(0.001)
	