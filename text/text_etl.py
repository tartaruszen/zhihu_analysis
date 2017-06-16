from text_config import get_config
config = get_config()
rt = config['rt']
rp = config['rp']
db = config['db']

topic = db.topic
question = db.question
question_answer = db.question_answer
answer_comment = db.answer_comment

def load_text(topic_token):
	return True