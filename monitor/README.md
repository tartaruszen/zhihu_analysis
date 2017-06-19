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

只修改配置是不够的, 因为像feed:6062 这样的网络地址, promethus并不认识, 因此需要指定外部网络, 通过在docker-compose.yml.2 文件中指定外部网络:
```
networks:
  docker_back-tier:
    external:
      name: docker_back-tier
```
docker_back-tier的命名来自于启动app时创建的网络名.

这样通过docker-compose启动的监视器就可以访问同样通过docker-compose启动的app了

```
$ docker-compose  up 
```

可以通过访问: http://localhost:9090/graph 来查看metrics.
