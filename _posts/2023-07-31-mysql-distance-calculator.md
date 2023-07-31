---
layout:     post
title:      "mysql距离计算"
subtitle:   "距离计算"
date:       2023-07-31 15:00:00
author:     "Andrew"
catalog: false
header-style: text
tags:
  - mysql
  - 经纬度
---
```sql
 
 CREATE TABLE `points` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `location` point DEFAULT NULL,
  `lng` varchar(255) DEFAULT NULL,
  `lat` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_local` (`location`(25))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

INSERT INTO  `points` (`id`, `location`, `lng`, `lat`, `name`) VALUES (1, ST_GeomFromText('POINT(113.305871 23.146077)'), '113.305871', '23.146077', '广州动物园');
INSERT INTO  `points` (`id`, `location`, `lng`, `lat`, `name`) VALUES (2, ST_GeomFromText('POINT(113.390965 23.055686)'), '113.390965', '23.055686', '小谷围岛');


-- 查询 越秀金融大厦与广州动物园距离 3km+ , 距离小谷围岛 10km+
 -- 方法一、 存储是  ponit类型
SELECT
 name ,
	ST_Distance (
		location,
	POINT ( 113.326318, 23.123985 )) * 111195 AS distance 
FROM
	points 
   HAVING  distance < 5000;
	 
	
 -- 方法二、 存储是  数字 
SELECT
 name ,
	ST_Distance (
		 POINT ( lng, lat ),
	POINT ( 113.326318, 23.123985 )) * 111195 AS distance 
FROM
	points 
   HAVING  distance < 5000; 
```