# NDK构建
---

## Android.mk 

一个 Android.mk文件是一个很小的构建脚本。你编写它以描述你给NDK构建器的源码文件们。它的语法在docs/ANDROID-MK.html中有详细描述。

NDK简单的将你的原文件组织到多个”模块”中，每个模块可以是以下的任意一种：

- 一个静态库
- 一个共享库

你可以在一个Android.mk中定义多个模块，或写多个Android.mk文件，每个文件只对应一个模块。

注意，一个Android.mk文件可能被构建系统分析多遍，所以不要假设某个变量没有被定义。默认下，NDK将寻找下面的构建脚本：

    $PROJECT/jni/Android.mk

如果你想在子路径下定义Android.mk文件，你应该在顶层的Android.mk中包含它们。有个函数可以做到这个功能：

    include$(call all-subdir-makefiles)

这将会包含当前构建路径的所有子路径下的Android.mk文件们。


## Application.mk

这个文件主要包含：

- 你的应用所需要模块的准确列表。
- 产生的机器码所对应的CPU架构。
- 可选的信息，像你要构建release还是debug，特殊的C或 C++编译参数以及其它需要应用到所有模块的构建选项。

例如要为ndk代码添加include<iostream>的支持：

```
#stl port
APP_STL := gnustl_static
```

这个文件是可选的：默认情况下，NDK将构建在Android.mk中列出的所有模块的并且默认面向CPUABI (armeabi).

将它放在$PROJECT/jni/Application.mk位置，那么它会被’ndk-build’脚本自动使用。


## ndk-build命令

    $ ndk-build          # 执行构建脚本
    $ ndk-build clean    # 清空所构建的二进制文件
    $ ndk-build -B V=1   # 强制性的重新编译并显示命令


--* 2015-06-05 update *--

## 使用命令行创建项目

1. SDK根目录下执行 tools/android list targets

2. 执行创建命令：

```
android create project --target <target-id> --name MyFirstApp \
--path <path-to-workspace>/MyFirstApp --activity MyActivity \
--package com.example.myfirstapp
```
<target-id>为第一步里展示的。


-- *2015-07-28 update* --

## 使用ant命令行打包

首先确保安装了ANT到环境，加入ANT_ROOT/bin到环境变量

```
android update project --name <project name> --target <target_id> --path <path_for_project>
# 这样就会产生build.xml, local.properties两文件。
# 如果添加了第三方包，需要添加--subprojects参数

ant debug # 打包一个测试apk  默认使用debug key签名
ant release # 生成一个未签名和未aligned的apk

adb install -r ./bin/XXX.apk  # adb 安装
```
