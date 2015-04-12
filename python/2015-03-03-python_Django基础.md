# Django 基础
---

## 1. 介绍


## 2. 安装，测试

	$ pip install django
	...
	$ python
	...
	>>> import django
	>>> django.VERSION
	(1, 7, 5, 'final', 0)	


## 3. 创建第一个项目

	$ django-admin startproject mysite

执行：

	$ python manage.py runserver
	$ python manage.py runserver 8080  # 指定一个端口
	$ python manage.py runserver 0.0.0.0:8000


## 4. 数据模型

在settings.py里设置：

```python
	'ENGINE': 'django.db.backends.mysql',
	'NAME': 'djangodb',
	'USER': 'root',
	'PASSWORD': 'passwd',
	'HOST': '',
	'PORT': '',
```

	$ python manage.py startapp blog

在blog/models.py:

```python
from django.contrib import admin
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
```

	$ python manage.py makemigrations polls

他告诉Django我有改变模型，需要将改变存储到migration。

	$ python manage.py migrate

执行所有migration里的操作，这里就为我们添加了表blog_blogpost。


## 5. admin

	$ python manage.py createsuperuser

创建admin后台超级账户。

/blog/models.py里添加：

```sql
# 添加后台展示列表式样
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)
```


## 6. Template 模板

一般规则是：

写模板，创建Template对象，创建Context对象，调用render( c )
```python
def index_template(request):
    t = loader.get_template('index.html')
    c = Context({'name': "Richard"})
    html = t.render(c)
    return HttpResponse(html)
```


