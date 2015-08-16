# java基本语法
---

## Doc

### javadoc 命令

```shell
    # 使用它生成html，源代码中“/**”的注释将出现在文档中
    # 并且只有public和protected的注释会被文档记录
    javadoc src/*.java -encoding UTF-8 -charset UTF-8
```

## 控制语句

for each 语法用于数组和容器
```java
    for (char c : "ABCEEDE EDGH".toCharArray()) {
        System.out.print(c + " ");
    }
```


### 静态导入

方式：
```java
import static 包名.类名.静态成员变量;
import static 包名.类名.静态成员函数;
```
注意导入的是成员变量和方法名。



