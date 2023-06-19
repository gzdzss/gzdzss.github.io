---
layout:     post
title:      "Macos ulimit 配置"
subtitle:   "ulimit"
date:       2023-06-19 18:00:00
author:     "Andrew"
catalog: false
header-style: text
tags:
  - Macos 
---
```text
方法一：
sudo launchctl limit maxfiles 65535 65535

方法二：
查看
sysctl kern.maxfiles
Sysctl kern.maxfilesperproc
ulimit -n
配置
sysctl  -w kern.maxfiles=65535
Sysctl -w kern.maxfilesperproc=65535
ulimit -n 65535
```