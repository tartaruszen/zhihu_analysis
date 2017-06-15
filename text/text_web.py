from flask import Flask
import redis

#r = redis.StrictRedis(host='redis-text', port=6380, db=0)
app = Flask(__name__)

rp = redis.StrictRedis(host='redis-pubsub', port=6379, db=0)

@app.route('/keyword/<topic_token>')
def show_user_profile(topic_token):
	if rp.exists('keyword'+str(topic_token)):
		keywords = rp.lrange('keyword'+str(topic_token),0,29)
		d = {}
		for k in keywords:
			d[k.split(':')[0]] = k.split(':')[1]
		return d
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