#-*- encoding:utf-8 -*-
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

import re
import jieba
import jieba.analyse

# import codecs
# from textrank4zh import TextRank4Keyword, TextRank4Sentence

def extract_keyword(text):
	text = re.sub('<[^>]+>','',text)
	jieba.analyse.set_stop_words("stop_words.txt")
	kw = jieba.analyse.extract_tags(text, topK=30, withWeight=True)
	keyword_d = {}
	for k,v in kw:
		keyword_d[k] = v
	return keyword_d

# def summarize(text):
	# keyword = {}
	# phrases = []
	# sentences = {}
	# tr4w = TextRank4Keyword()
	# tr4w.analyze(text=text, lower=True, window=2) 
	# for item in tr4w.get_keywords(20, word_min_len=1):
		# print(item.word, item.weight)
		# keyword[item.word] =  item.weight
	# for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
		# print(phrase)
		# phrases.append(phrase)
	# tr4s = TextRank4Sentence()
	# tr4s.analyze(text=text, lower=True, source = 'all_filters')
	# for item in tr4s.get_key_sentences(num=3):
		# print(item.index, item.weight, item.sentence)
		# sentences[item.index] = item.weight+''+item.sentence
	# return {'keyword':keyword,'phrases':phrases,'sentences':sentences}