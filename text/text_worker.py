import time
from text_etl import load_text
from text_analysis import extract_keyword

from text_config import get_config
config = get_config()
rt = config['rt']
rp = config['rp']
rpp = rp.pubsub()

rpp.subscribe('craw-to-text')

if __name__ == '__main__':
	while True:
		message = rpp.get_message()
		if message:
			print 'text_worker process!'
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
		print 'text_worker wait!'
		time.sleep(0.001)
