import re
import jieba
import jieba.analyse

def extract_keyword(text):
	text = re.sub('<[^>]+>','',text)
	kw = extractKeyphrases(text)
	jieba.analyse.set_stop_words("stop_words.txt")
	kw = jieba.analyse.extract_tags(text, topK=30, withWeight=True)
	keyword_d = {}
	for k,w in kw:
		keyword_d[k] = v
	return keyword_d