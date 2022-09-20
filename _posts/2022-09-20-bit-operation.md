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

    binaryString(t1);
    binaryString(t2);
    binaryString(t3);
    binaryString(t4);
    binaryString(t5);
    binaryString(t6);
    binaryString(t7);

    System.out.println("======");
    
    //开启t1, t3
    int tmp = t1 + t3;

    binaryString(tmp);
    
    //判断开启了 t1
    System.out.println((tmp & t1) == t1);
    //判断开启了 t3
    System.out.println((tmp & t3) == t3);
    //判断同时开启了 t1,t3
    System.out.println((tmp & (t1 + t3)) == (t1 + t3));

    System.out.println("======");
    
    //再追加开启t2
    tmp = (tmp + t2);

    //打印二进制
    binaryString(tmp);

    //判断开启了 t2
    System.out.println((tmp & t2) == t2);

    //判断同时开启了 t1,t2, t3
    System.out.println((tmp & (t1 + t2 + t3)) == (t1 + t2 + t3));

    //关闭t3 开启t5
    tmp = tmp - t3 + t5;

    //判断同时开启了 t1,t2 
    System.out.println((tmp & (t1 + t2)) == (t1 + t2));

    //判断同时开启了 t5
    System.out.println((tmp & (t5)) == (t5));

    //判断同时开启了 t4
    System.out.println((tmp & (t4)) == (t4));
}

/**
 * 打印二进制
 * mysql转二进制 ：  select bin(67) from dual;
 *
 * @param num
 */
public static void binaryString(int num) {
    String binaryString = Integer.toBinaryString(num);
    System.out.println(num + " -> " + binaryString);
}

```

> 输出结果

```text
1 -> 1
2 -> 10
4 -> 100
8 -> 1000
16 -> 10000
32 -> 100000
64 -> 1000000
======
5 -> 101
true
true
true
======
7 -> 111
true
true
true
true
false
```

