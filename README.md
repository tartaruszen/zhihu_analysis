# zhihu_analysis
zhihu_analysis api services
1. kong services:api-gateway load-balance logs authentication

2. text services: text analysis

3. graph services: graph analysis

4. craw services: craw zhihu

5. monitor services

# program architecture
![program architecture](https://github.com/phiedulxp/zhihu_analysis/blob/master/pic/zhihu.png)

# useage

1. ./docker-compose up for services

2. ./monitor docker-compose up for monitor services

see [/monitor/README.md](https://github.com/phiedulxp/zhihu_analysis/blob/master/monitor/README.md) for detail

then you will see kong-dashboard on http://localhost:8081 at http://you-host-ip:8001

![api](https://github.com/phiedulxp/zhihu_analysis/blob/master/pic/api.png)
![comsumer](https://github.com/phiedulxp/zhihu_analysis/blob/master/pic/comsumer.png)
![plugin](https://github.com/phiedulxp/zhihu_analysis/blob/master/pic/plugin.png)

## api requests demo:

```
## from Host
r = requests.get('http://localhost:5001')
r.json()
{u'/keyword/topic_token': u'return top 30 keywords in the topic'}

## from api-gateway
r = requests.get('http://localhost:8000',headers={'Host':'text','apikey':'key-text'})
r.json()
{u'/keyword/topic_token': u'return top 30 keywords in the topic'}

## authentication
r = requests.get('http://localhost:8000',headers={'Host':'text','apikey':'key'})
r.json()
{u'message': u'Invalid authentication credentials'}

## Host route
r = requests.get('http://localhost:8000',headers={'Host':'tttt','apikey':'key-text'})
r.json()
{u'message': u'no API found with those values'}

## get zhihu topic hot text keyword
r = requests.get('http://localhost:8000/keyword/20023491',headers={'Host':'text','apikey':'key-text'})
r.text
u'topic 20023491'

## wait for a moment
r = requests.get('http://localhost:8000/keyword/20023491',headers={'Host':'text','apikey':'key-text'})
r.text
u'topic 20023491'
```

