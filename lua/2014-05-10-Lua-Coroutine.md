# Lua Coroutine (协同式多线程)
---

## 基本概念

Lua 为每个 coroutine 提供一个独立的运行线路。 然而和多线程系统中的线程不同，coroutine 只在显式的调用了 yield 函数时才会挂起。

创建: coroutine.create

运行: 第一次使用coroutine.resume就可以把创建的coroutine运行起来。

终止: 一种是自身函数执行完了, 另一种是非正常退出，它发生在未保护的错误发生的时候。 第一种情况中， coroutine.resume 返回 true ， 接下来会跟着 coroutine 主函数的一系列返回值。 第二种发生错误的情况下， coroutine.resume 返回 false ， 紧接着是一条错误信息。

切换: coroutine.yield可以切换出去，resume可以使其返回。

状态: 协程有4种状态，suspended, running, dead, normal (可以coroutine.status(co)来查看)

coroutine.wrap(): 创建coroutine，返回一个函数，一旦你调用这个函数，就进入coroutine，和create功能重复

coroutine.running() : 返回正在跑的coroutine，一个coroutine就是一个线程，当使用running的时候，就是返回一个corouting的线程号

## 例子：

### 1. 切换和状态

```lua
local function foo(sumNum, yieldNum)
    for i=1,sumNum do
        print("co", i)
        if i == yieldNum then
            coroutine.yield()
        end
    end
end

local co = coroutine.create(foo)
coroutine.resume(co, 10, 5)
print(coroutine.status(co))
coroutine.resume(co)
print(coroutine.status(co))
print(coroutine.resume(co))
print(coroutine.status(co))
```
输出：
```
co	1
co	2
co	3
co	4
co	5
suspended
co	6
co	7
co	8
co	9
co	10
dead
false	cannot resume dead coroutine
dead
[Finished in 0.0s]
```

### 2. coroutine.wrap

```lua
local function foo(sumNum, yieldNum)
    for i=1,sumNum do
        print("co", i)
        if i == yieldNum then
            coroutine.yield()
        end
    end
end

local co = coroutine.wrap(foo)
co(10, 5)
```

输出：
```
co	1
co	2
co	3
co	4
co	5
[Finished in 0.0s]
```


## 参考资料

> + [lua5.1-manual](http://www.codingnow.com/2000/download/lua_manual.html)

> + [Lua程序设计第二版]
