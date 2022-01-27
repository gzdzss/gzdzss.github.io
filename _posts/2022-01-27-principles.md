---
layout:     post
title:      "浅谈软件设计原则"
subtitle:   "所谓的设计原则就是在大量的工程实践的基础上以及科学研究的基础上总结出来的一些经验和理念。"
date:       2022-01-27 15:29:00
author:     "Andrew"
catalog: false
header-style: text
tags:
  - 设计原则 
---


> 首先，为什么要有软件设计原则？软件设计原则的目的是为了让我们编写出更好的代码，那什么是“更好的代码”？“更好的代码”就是使代码更简洁、更易读、更具有可维护性以及更具有可扩展性。那么我们写代码或者设计代码结构的时候不遵循软件设计原则可以吗？答案是可以的。因为软件设计原则不像是Java语法一样的硬性要求，不这么做编译就不通过，你的程序就运行不了，相反，不遵循这七大设计原则你的代码照样能够运行。那么所谓的设计原则就是在大量的工程实践的基础上以及科学研究的基础上总结出来的一些经验和理念，我们在设计以及编写代码的过程中要尽量地借鉴前人的一些好的经验来使我们自己少走弯路，这也是软件设计原则的意义所在 [[1]](https://blog.csdn.net/u013655410/article/details/104410375)。

### 七大设计原则
1. [开闭原则](#1开闭原则 "开闭原则")
2. [依赖导倒置原则](#2依赖导倒置原则 "依赖导倒置原则")
3. [单一职责原则](#3单一职责原则 "单一职责原则")
4. [接口隔离原则](#4接口隔离原则 "接口隔离原则")
5. [迪米特原则](#5迪米特原则 "迪米特原则")
6. [里氏替换原则](#6里氏替换原则 "里氏替换原则")
7. [合成复用原则](#7合成复用原则 "合成复用原则")


### 1.开闭原则
> 开闭原则（Open Closed Principle，OCP）由勃兰特·梅耶（Bertrand Meyer）提出，他在 1988 年的著作《面向对象软件构造》（Object Oriented Software Construction）中提出：软件实体应当对扩展开放，对修改关闭（Software entities should be open for extension，but closed for modification），这就是开闭原则的经典定义。
>> ***即当应用的需求改变时，在不修改软件实体的源代码或者二进制代码的前提下，可以扩展模块的功能，使其满足新的需求。***

示例[[2]](https://baijiahao.baidu.com/s?id=1670636817035694210&wfr=spider&for=pc)：

> 假设有一个水果店，该水果店现在出售：“苹果、香蕉。”
>> 水果基类
```java
/**
 * 基类
 */
public abstract class Fruit {
    protected int type;
}
/**
 * 苹果
 */
public class Apple extends Fruit {
    public Apple() {
        this.type = 1;
    }
}
/**
 * 香蕉
 */
public class Banana extends Fruit {
    public Banana() {
        this.type = 2;
    }
}
```
>> 水果店
```java
public class FruitShop {
    public void sellFruit(Fruit fruit) {
        if (fruit.type == 1) {
            sellApple(fruit);
        } else if (fruit.type == 2) {
            sellBanana(fruit);
        }
    }
    private void sellApple(Fruit fruit) {
        System.out.println("卖出了一斤苹果！");
    }
    private void sellBanana(Fruit fruit) {
        System.out.println("卖出了一斤香蕉！");
    }
}
```
>> 执行测试类
```java
    public static void main(String[] args) {
        FruitShop shop =  new FruitShop();
        shop.sellFruit(new Apple());
        shop.sellFruit(new Banana());
    }
//执行结果:
//卖出了一斤苹果！
//卖出了一斤香蕉！
```

> 现在水果店扩张，添加了一种新的水果（西瓜）。根据以上示例代码我们需要作出如下新增。
>> 1、新增西瓜类
```java
/**
 * 西瓜
 */
public class Watermelon extends Fruit {
    public Watermelon() {
        this.type = 3;
    }
}
```
>> 2.FruitShop类中添加“卖西瓜”的方法
```java
public class FruitShop {
    ...
    private void sellWatermelon(Fruit fruit) {
        System.out.println("卖出了一斤西瓜！");
    }
}
```
>> 3.修改FruitShop类中的sellFruit方法
```java
 public void sellFruit(Fruit fruit) {
        ...
        } else if (fruit.type == 3) {
            sellWatermelon(fruit);
        }
    } 
```
>> 4.执行测试类
```java
public static void main(String[] args) {
        FruitShop shop =  new FruitShop();
        shop.sellFruit(new Apple());
        shop.sellFruit(new Banana());
        shop.sellFruit(new Watermelon());
    }
//执行结果:
//卖出了一斤苹果！
//卖出了一斤香蕉！
//卖出了一斤西瓜！
```

通过以上三步就实现了增加一种水果的需求，但是大家有没有发现，这种方式虽然容易理解，可是当功能发生变动时，代码的修改量会特别大。并且这种方式也**不符合“开闭原则”**，大家能看出来吗？

> 我们可以将以上代码进行如下优化：
>> 1.水果基类添加抽象售卖方法
```java
public abstract class Fruit {
    ...
    public abstract void sell();
}
```
>> 2.水果店售卖改造
```java
public class FruitShop {
    public void sellFruit(Fruit fruit) {
        fruit.sell();
    }
}
```
>> 3.对应的水果改造
```java
public class Apple extends Fruit {
    @Override
    public void sell() {
        System.out.println("卖出类一斤苹果!");
    }
}
public class Banana extends Fruit {
    @Override
    public void sell() {
        System.out.println("卖出类一斤香蕉!");
    }
}
public class Watermelon extends Fruit {
    @Override
    public void sell() {
        System.out.println("卖出类一斤西瓜!");
    }
}
```
>> 4.执行测试方法
```java
public static void main(String[] args) {
        FruitShop shop =  new FruitShop();
        shop.sellFruit(new Apple());
        shop.sellFruit(new Banana());
        shop.sellFruit(new Watermelon());
    }
//执行结果:
//卖出了一斤苹果！
//卖出了一斤香蕉！
//卖出了一斤西瓜！
```

demo地址:[https://github.com/gzdzss/blog-demo/tree/main/software-design-principles/src/main/java/ocp](https://github.com/gzdzss/blog-demo/tree/main/software-design-principles/src/main/java/ocp)

这样优化后的代码就**遵守了“开闭原则”**。提供方可以对系统进行扩展（对扩展开放），当系统扩展了新的功能后不会影响到使用方，使用方不需要进行修改（对修改关闭）。

通过上面的描述相信大家能看出，“开闭原则”给我们传递的思想就是：尽量通过扩展软件的模块、类、方法，来实现功能的变化，而不是通过修改已有的代码来完成。这样做就可以大大降低因为修改代码而给程序带来的出错率。



### 2.依赖导倒置原则
> todo

### 3.单一职责原则
> todo

### 4.接口隔离原则
> todo

### 5.迪米特原则
> todo

### 6.里氏替换原则
> todo

### 7.合成复用原则
> todo




### 参考文献
- [[1]浅谈软件设计的七大原则·Daemon Zhang](https://blog.csdn.net/u013655410/article/details/104410375)
- [[2]作为程序员不可不会的设计模式七大原则之——“开闭原则”·编程小菜鸟](https://baijiahao.baidu.com/s?id=1670636817035694210&wfr=spider&for=pc)
