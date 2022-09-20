---
layout:     post
title:      "位运算"
subtitle:   "采用位运算来判断开关"
date:       2022-09-20 11:00:00
author:     "Andrew"
catalog: false
header-style: text
tags:
  - 位运算 
---

```java
 public static void main(String[] args) {
        int t1 = 1;
        int t2 = 1 << 1;
        int t3 = 1 << 2;
        int t4 = 1 << 3;
        int t5 = 1 << 4;
        int t6 = 1 << 5;
        int t7 = 1 << 6;

        System.out.println(t1);
        System.out.println(t2);
        System.out.println(t3);
        System.out.println(t4);
        System.out.println(t5);
        System.out.println(t6);
        System.out.println(t7);

        System.out.println("======");

        //开启t1, t3
        int tmp = t1 + t3;

        System.out.println(tmp);
        System.out.println("======");
        //二进制
        System.out.println(Integer.toBinaryString(tmp));
        //mysql转二进制 ：  select bin(67) from dual;
        System.out.println("======");

        //判断开启了 t1
        System.out.println((tmp & t1) == t1);
        //判断开启了 t3
        System.out.println((tmp & t3) == t3);

        //判断同时开启了 t1,t3
        System.out.println((tmp & (t1 + t3)) == (t1 + t3));

        //判断开启了 t2
        System.out.println((tmp & t2) == t2);
    }
```

> 输出结果

```text
1
2
4
8
16
32
64
======
5
======
101
======
true
true
true
false
```

