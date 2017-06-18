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
	topic_corpora = u''
	topic_ = topic.find_one({'topic_token':topic_token})
	topic_corpora = topic_corpora+topic_['data']['name']
	qtl = topic_['question_token_list']
	for qt in qtl:
		q_ = question.find_one({'question_token':qt})
		topic_corpora = topic_corpora+' '+q_['questions']['title']
		qa_ = question_answer.find_one({'question_token':qt})
		for qai in qa_['answers']['items']:
			topic_corpora = topic_corpora+' '+qai['content']
			at = qai['id']
			ac_ = answer_comment.find_one({'answer_token':at})
			for aci in ac_['answers']['items']:
				topic_corpora = topic_corpora+' '+aci['content']
	rt.set('corpora'+topic_token,topic_corpora)