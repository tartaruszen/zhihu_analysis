### Monitor

#### 配置监视器

在启动 monitor 之前,需要在prometheus/prometheus.yml文件中添加target, 默认情况下, 它的配置为:

```
 - targets: ['localhost:9090','cadvisor:8080']
```

可见, prometheus只监视自身 和 cadvisor导出的docker daemon上所有容器层的metrics. 如果之前通过/docker/docker-compose.yml启动了我们的应用, 那么可以修改该配置为:

```
- targets: ['localhost:9090','cadvisor:8080','redis-pubsub:6379','mongo-crawer:27017','mongo-crawer:28017','redis-text:6379','text:5000','consul:8500','kong-database:5432','kong:8000','kong:8443','kong:8001','kong:7946','kong-dashboard:8080']
```

这样通过docker-compose启动的监视器就可以访问同样通过docker-compose启动的app了

```
$ docker-compose  up 
```

可以通过访问: http://localhost:9090/graph 来查看metrics.

#### 可视化

可视化采用grafana, 它与prometheus结合的很好, 采用该方案可以很好的监控docker容器的状态

打开浏览器 [http://localhost:3000](http://localhost:3000), 进入grafana, 添加数据源, Type选择Prometheus, Access选择direct模式, 填写prometheus的url: http://localhost:9090, 勾上默认. Save & test. 退出.

添加dashboard, 导入monitor/grafana/docker_dashboard.json 即可看到下图:

![docker_dashboard](https://github.com/buptmiao/microservice-app/blob/master/pictures/docker_dashboard.png) 
