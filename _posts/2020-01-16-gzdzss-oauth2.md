---
layout:     post
title:      "Oauth2实践"
subtitle:   "oatuh2实践，分为单机本，与分布式版本"
date:       2020-01-16 15:39:00
author:     "周雁杰"
catalog: false
header-style: text
tags:
  - Oauth2
---

[gzdzss-oauth2](https://github.com/gzdzss/gzdzss-oauth2)  

# oauth2整合

## eureka-server  注册中心     

## [gzdzss-order 订单模块](https://github.com/gzdzss/gzdzss-oauth2/tree/master/gzdzss-order)

## [gzdzss-storage 库存模块](https://github.com/gzdzss/gzdzss-oauth2/tree/master/gzdzss-storage)

## [gzdzss-authserver 认证中心](https://github.com/gzdzss/gzdzss-oauth2/tree/master/gzdzss-authserver) 

## [gzdzss-gateway 服务网关](https://github.com/gzdzss/gzdzss-oauth2/tree/master/gzdzss-gateway)


## 架构图

![image](https://github.com/gzdzss/gzdzss-oauth2/raw/master/oauth2.png)


## 分支

### [1.0.0.RELEASE](https://github.com/gzdzss/gzdzss-oauth2/tree/1.0.0.RELEASE) 单一版（无注册中心）


### [2.0.0.RELEASE](https://github.com/gzdzss/gzdzss-oauth2/tree/2.0.0.RELEASE) 集群版本 （添加注册中心， feign, hystrix）


##配套前台demo页面  （vue 2.0,  vuex , vue-route, axios）

[gzdzss-web](https://github.com/gzdzss/gzdzss-web)

- 登录
- 自动刷新token  (配置认证中心 oauth_client_details (access_token_validity)  设置为60s,可验证每次先刷新再调用)
- 注销
- 接口调用