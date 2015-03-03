# Virtualenv 虚拟环境
---

virtualenv用于创建独立的python环境，使这个虚拟环境与外界相独立。

## 1. virtualenv

### 安装

pip的安装方式：

	$ sudo pip install virtualenv

### 创建虚拟环境

	$ virtualenv envname

默认情况下，虚拟环境会依赖系统环境中的site packages. 如不要这些package，需要添加参数：--no-site-packages. (MAC下第三方包都在/Library/Python/2.7/site-packages 下)

	$ virtualenv --no-site-packages envname

virtualenv里附带了pip的安装工具，所以需要在虚拟环境中安装其他套件可以用pip.

安装的新包将在：envname/lib/python2.7/site-packages

### 启动与退出虚拟环境

	$ cd envname
	$ source ./bin/active    # 启动
	(envname)$ deactivate    # 退出

  
---

## 2. 安装virtualenvwrapper

virtualenvwrapper是virtualenv的拓展包，用于方便管理虚拟环境。

+ 将所有虚拟环境整合在一个目录下 
+ 管理（新增，删除，复制）虚拟环境 
+ 快速切换虚拟环境 
+ tab补全虚拟环境名字 
+ 每個操作都提供允许使用者自己定制的hooks 
+ 可以编写比较容易分享的extension plugin Tab 補全虛擬環境的名字。 每個操作都提供允許使用者自訂的 hooks。 可撰寫容易分享的 extension plugin 系統。 

### 安装

	$ sudo pip install virtualenvwrapper
	$ mkdir ~/.virtualenvwrapper

将下列代码加入到.bash_profile或者.zshrc中去：（MAC）

```
# Add for python virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs  # virtualenv install place
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
source /usr/local/bin/virtualenvwrapper.sh
```

### 创建，启用，切换，退出，删除，列出列表等等

```
$ mkvirtualenv envname    # 创建
$ workon envname          # 启动/切换
$ rmvirtualenv envname    # 删除
$ deactivate              # 退出
$ workon				  # 列表
$ lsvirtualenv			  # 列表
```

### 其他

启动虚拟环境后，你可以安装任何套件。

	(envname)$ pip install django
	...
	(envname)$ lssitepackages    # 展示envname环境下第三方包
	Django-1.7.5.dist-info ...
	...


## 参考资料:
> + [virtualenv](https://virtualenv.pypa.io/en/latest/) 
> + [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html)


