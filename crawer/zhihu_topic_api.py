import requests
from bs4 import BeautifulSoup

from craw_config import get_config
config = get_config()
db = config['db']

topic = db.topic
question = db.question
question_answer = db.question_answer
answer_comment = db.answer_comment

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
          'authorization':'Bearer Mi4wQUJES2V4VTJGd2tBUUlKaDFUMHJDeGNBQUFCaEFsVk5iUjlIV1FCTWJlYlFVemVUSUxxZFlpNTVIRGRiYTQ5U3d3|1497493211|bfcfd074d07a691bdfe92a980ff4eb770a918cd8'
          }
zhihu_api = 'https://www.zhihu.com/api/v4/'
zhihu_api_topics = zhihu_api+'/topics/{}?include=introduction%2Cquestions_count%2Cbest_answers_count%2Cfollowers_count%2Cis_following'
zhihu_api_topics_top_answers = 'https://www.zhihu.com/topic/{}/top-answers?page={}'
zhihu_api_questions = zhihu_api+'questions/{}'
zhihu_api_answers = zhihu_api+'answers/{}'
zhihu_api_answers_comments = zhihu_api+'''answers/{}/comments?include=data%5B*%5D.author%2Ccollapsed%2C
reply_to_author%2Cdisliked%2Ccontent%2Cvoting%2Cvote_count%2Cis_parent_author%2C
is_author&order=normal&limit=20&offset=0&status=open'''
questions_answers_include = '''include=data%5B*%5D.is_normal%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics'''
zhihu_api_questions_answers = zhihu_api+'questions/{}/answers?limit=20&offset=0'+'&'+questions_answers_include
members_include = '''include=locations%2Cemployments%2Cgender%2Ceducations%2Cbusiness%2Cvoteup_count%2Cthanked_Count%2Cfollower_count%2Cfollowing_count%2Ccover_url%2Cfollowing_topic_count%2Cfollowing_question_count%2Cfollowing_favlists_count%2Cfollowing_columns_count%2Cavatar_hue%2Canswer_count%2Carticles_count%2Cpins_count%2Cquestion_count%2Ccommercial_question_count%2Cfavorite_count%2Cfavorited_count%2Clogs_count%2Cmarked_answers_count%2Cmarked_answers_text%2Cmessage_thread_token%2Caccount_status%2Cis_active%2Cis_force_renamed%2Cis_bind_sina%2Csina_weibo_url%2Csina_weibo_name%2Cshow_sina_weibo%2Cis_blocking%2Cis_blocked%2Cis_following%2Cis_followed%2Cmutual_followees_count%2Cvote_to_count%2Cvote_from_count%2Cthank_to_count%2Cthank_from_count%2Cthanked_count%2Cdescription%2Chosted_live_count%2Cparticipated_live_count%2Callow_message%2Cindustry_category%2Corg_name%2Corg_homepage%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'''
zhihu_api_members = zhihu_api+'members/{}'+'?'+members_include

def get_data_from_zhihu_api(api,token):
    data = {'totals':0,'items':[]}
    res = requests.get(api.format(token),headers=headers)
    if res.status_code == 404:
        return {'error':'http_404'}
    try:
        j = res.json()
    except:
        return {'error':'no json'}
    if not 'offset' in api:
        return j
    else:
        try:
            data['totals'] = j['paging']['totals']
        except:
            data['totals'] = None
        data['items'].extend(j['data'])
        while not j['paging']['is_end']:
            res = requests.get(j['paging']['next'],headers=headers)
            j = res.json()
            data['items'].extend(j['data'])
        return data

def get_proxy():
    return requests.get("http://proxypool:8000").json()[0]
    #return requests.get("http://123.207.35.36:5000/get/").content

# def delete_proxy(proxy):
    # requests.get("http://proxy-pool:5000/delete/?proxy={}".format(proxy))

def get_topic_hot(topic_token):
    j = get_data_from_zhihu_api(zhihu_api_topics,topic_token)
    page = j['best_answers_count']/20 + 1
    question_token_list = []
    for p in xrange(page):
        r_ = requests.get(zhihu_api_topics_top_answers.format(topic_token,p+1),headers=headers,proxies={"http": "http://{}".format(get_proxy())})
        if r_.status_code == 404:
            continue
        soup = BeautifulSoup(r_.content,"html5lib")
        q = soup.find('div',attrs={'class':'zm-topic-list-container'}).find_all('a',attrs={'class':'question_link'})
        for i in q:
            question_token_list.append(i.attrs['href'].split('/')[-1])
    return j,list(set(question_token_list))

def get_answer_token(answers):
    answer_token_list = []
    for item in answers['items']:
        answer_token_list.append(int(item['url'].split('/')[-1]))
    return answer_token_list


def save_topic_all(topic_token):
    topic_token = str(topic_token)
    print 'topic_token:',topic_token
    if topic.find_one({'topic_token':topic_token}) == None:
        topic_j,question_token_list = get_topic_hot(topic_token)
        topic.insert_one({'_id':topic_token,'topic_token':topic_token,'data':topic_j,'question_token_list':question_token_list})
        for question_token in question_token_list:
            print 'question_token:',question_token
            if question.find_one({'question_token':question_token}) == None:
                questions = get_data_from_zhihu_api(zhihu_api_questions,question_token)
                question.insert_one({'_id':question_token,'question_token':question_token,'questions':questions})
                if question_answer.find_one({'question_token':question_token}) == None:
                    answers = get_data_from_zhihu_api(zhihu_api_questions_answers,question_token)
                    question_answer.insert_one({'_id':question_token,'question_token':question_token,'answers':answers})
                    answer_token_list = get_answer_token(answers)
                    for answer_token in answer_token_list:
                        if answer_comment.find_one({'answer_token':answer_token}) == None:
                            answer_comments = get_data_from_zhihu_api(zhihu_api_answers_comments,answer_token)
                            answer_comment.insert_one({'_id':answer_token,'answer_token':answer_token,'answers':answer_comments})
        return True
    else:
        return True
