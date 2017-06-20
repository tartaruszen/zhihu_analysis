# zhihu_analysis
zhihu_analysis api services
1. kong services:api-gateway load-balance logs authentication  【吴汇哲】

2. text services: text analysis  【胡源达】

3. graph services: graph analysis 【todo】

4. craw services: craw zhihu  【黎谢鹏】

5. monitor services   【王通杰】

# online demo [校园局域网]

[Kong-dashboard](http://219.228.60.97:8081/)  set http://219.228.60.97:8001/


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
r.json()
{
API:"0.0867107072112"
Cloud:"0.0276468921543"
SOA:"0.0540371073925"
Spring:"0.0389569843992"
agent:"0.0251335383221"
cloud:"0.0351869536509"
docker:"0.0339302767348"
php:"0.0251335383221"
spring:"0.0464970458959"
业务:"0.0452019619729"
公司:"0.0327771286638"
分布式:"0.0348973139995"
创业:"0.0323071570427"
复杂度:"0.0339302767348"
实例:"0.0267745595504"
客户端:"0.0647108703668"
异步:"0.0350657719959"
技术:"0.0664782152768"
服务:"0.283027846202"
架构:"0.109926044733"
注册:"0.0390894301324"
系统:"0.0354559236344"
组件:"0.0561964340661"
网关:"0.047753722812"
请求:"0.0306652675587"
调用:"0.0372487675362"
负载:"0.0323511931278"
轮子:"0.0442633816582"
选型:"0.0363616447341"
部署:"0.0296247312037"
}
```
## reference
[微服务架构](https://www.zhihu.com/topic/20023491/top-answers)【知乎topic】

![20023491](https://github.com/phiedulxp/zhihu_analysis/blob/master/pic/20023491.png)
