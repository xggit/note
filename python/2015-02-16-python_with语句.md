# Python的with语句
---

python 2.5以后增加了with表达式的语法。

这里牵出一个概念：上下文管理器（Context Manager）：实现了\_\_enter\_\_() 和\_\_exit\_\_() 方法的对象。上下文管理器定义执行 with 语句时要建立的运行时上下文, 负责执行 with 语句块上下文中的进入与退出操作。通常使用 with 语句调用上下文管理器, 也可以通过直接调用其方法来使用。

所以上下文管理器对象基本的形式如下：
```python
class controlled_execution:
    def __enter__(self):
        set things up
        return things
    def __exit__(self, type, value, traceback):   # type,value,traceback是异常时才会传入的，
												  # 没有异常就为None,None,None
        tear things down
         
with controlled_execution() [as things]:
        do something
```
python会首先运行enter里的代码，返回things，作为as 后面的变量值，然后再运行with模块中的代码，最后会自动执行exit中的代码，而不管with中的代码运行结果如何。它能简化try-finally语句。所以with通常用在读取文件的操作中，将文件句柄的关闭操作放在exit方法中，这样就不会因忘记释放文件句柄而产生可能出现的错误。

另外as things的things可以是单个变量，或者由“()”括起来的元组（不能是仅仅由“,”分隔的变量列表，必须加“()”）。

with表达式还可以嵌套：
```python
with A() as a, B() as b:
    suite
# 等价于
with A() as a:
    with B() as b:
	        suite
```

**Python 对一些内建对象进行改进，加入了对上下文管理器的支持，可以用于 with 语句中，比如可以自动关闭文件、线程锁的自动获取和释放等**。

例如，对文件的操作：
```python
with open(r'somefileName') as somefile:
	for line in somefile:
		print line
		# ...more code
```
这里不管在处理文件过程中是否发生异常，都能保证 with 语句执行完毕后已经关闭了打开的文件句柄。
   
    
---
更新：

## contextlib模块
contextlib 模块提供了3个对象：装饰器 contextmanager、函数 nested 和上下文管理器 closing。使用这些对象，可以对已有的生成器函数或者对象进行包装，加入对上下文管理协议的支持，避免了专门编写上下文管理器来支持 with 语句。

### 1. @contextmanager
contextmanager 用于对生成器函数进行装饰，生成器函数被装饰以后，返回的是一个上下文管理器，其 __enter__() 和 __exit__() 方法由 contextmanager 负责提供，而不再是之前的迭代子。被装饰的生成器函数只能产生一个值，否则会导致异常 RuntimeError；如果使用了 as 子句的话, 产生的值会赋值给 as 子句中的 target。

```python
from contextlib import contextmanager

@contextmanager
def demo():
    print "run demo"
    yield '*** contextmanager demo ***'
    print "end demo"

with demo() as value:
    print "================"
    print 'Assigned Value: %s' % value
    print "----------------"
```
这里要注意他们的输出顺序,查看输出：
```
run demo
================
Assigned Value: *** contextmanager demo ***
----------------
end demo
```

### 2. nested
nested函数的作用就是将多个上下文管理器组织在一起，避免使用嵌套 with 语句。
    
	with nested(A(), B(), C()) as (X, Y, Z):
         # with-body code here

需要注意的是，发生异常后，如果某个上下文管理器的 __exit__() 方法对异常处理返回 False，则更外层的上下文管理器不会监测到异常。

### 3. closing上下文管理器
closing上下文管理器会将包装的对象赋值给 as 子句的 target 变量，同时保证打开的对象在 with-body 执行完后会关闭掉。closing 上下文管理器包装起来的对象必须提供 close() 方法的定义，否则执行时会报 AttributeError 错误。closing 适用于提供了 close() 实现的对象，比如网络连接、数据库连接等，也可以在自定义类时通过接口 close() 来执行所需要的资源“清理”工作。

```python
import urllib, sys
from contextlib import closing

with closing(urllib.urlopen('http://www.yahoo.com')) as f:
    for line in f:
        sys.stdout.write(line)
```

  


## 参考资料：
> + [官方文档](https://docs.python.org/2/reference/compound_stmts.html#the-with-statement)
> + [官方文档](https://docs.python.org/2/reference/datamodel.html#context-managers)
> + [IBM developerWorks文章](https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith)

