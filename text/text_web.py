from flask import Flask
import json
import os
app = Flask(__name__)

from text_config import get_config
config = get_config()
rt = config['rt']
rp = config['rp']
rpp = rp.pubsub()

@app.route('/')
def hello():
	message = {'/keyword/topic_token':'return top 30 keywords in the topic'}
	return json.dumps(message)

@app.route('/keyword/<topic_token>')
def show_user_profile(topic_token):
	if rt.exists('keyword'+str(topic_token)):
		keywords = rt.lrange('keyword'+str(topic_token),0,29)
		d = {}
		for k in keywords:
			d[k.split(':')[0]] = k.split(':')[1]
		print d
		return json.dumps(d)
		# html = '<ol>'
		# for k in keywords:
			# html = html+'<li>'+k+'</li>'
		# html = html+'</ol>'
		# return html
	else:
		rp.publish('text-to-craw',str(topic_token))
	return 'topic %s' % topic_token

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)