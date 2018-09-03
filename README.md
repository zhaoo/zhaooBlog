# zhaooBlog

zhaooBlog 是一个基于Django 开发的个人博客系统。

[![Verson](https://img.shields.io/badge/Release-1.0.0-orange.svg)](https://github.com/izhaoo/zhaooBlog)
[![Python](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Django](https://img.shields.io/badge/Django-2.1.1-green.svg)](https://docs.djangoproject.com/en/2.1/releases/2.1.1/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](https://mit-license.org/)

* [预览](http://zhaooblog.izhaoo.com)

## 介绍

最近在学习Vue.js ，需要后端配合返回JSON ，所以就顺便学习了Django ，花了两天时间写了这么一个博客系统。该博客系统基本功能齐全，UI 简洁，花里胡哨的不要搞，只能这么说了。由于本人技术及时间有限，该博客系统仅仅是作为一个练手的小玩具而诞生的，不建议投入实际使用，仅供代码参考。

### 插件库

* 前端： jQuery, Bootstrap, Font Awesome, FancyBox, particles.js
* 后端： Django, django-mdeditor, markdown, Pygments

### 图片预览

![首页](https://pic.izhaoo.com/20180902093948.jpg)
![文章页](https://pic.izhaoo.com/20180902094025.jpg)
![后台](https://pic.izhaoo.com/20180902094058.jpg)

## 功能

|模块| 功能|
|:------:|:------:|
|首页|访问量统计, 分页|
|文章|Markdown, 代码高亮, 评论|
|标签|标签云|
|归档|时间轴|
|其他|Sitemap, RSS|

## 安装

[![开发环境](https://img.shields.io/badge/%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83-Win-blue.svg)]()

### 安装 Python3.7

安装Python3.7 ，[Python官网](https://www.python.org/downloads/release/python-370/)。 

### 安装 Virtualenv

```
pip install virtualenv    # 安装Virtualenv

makdir dango_web    # 创建网站目录
cd django_web    # 移动到目录
virtualenv env    # 创建env虚拟目录
env\Scripts\activate.bat    # 激活虚拟环境
```

### 下载 zhaooBlog

```
makdir blog    # 创建项目容器
cd blog    # 移动到容器
git clone https://github.com/izhaoo/zhaooBlog    # 克隆到本地
```

当然也可在本页面下载Zip 文件，解压到目录内。

### 安装依赖

项目所用到的依赖都已经写在`requirements.txt`文件内，直接安装即可。

```
pip install requirements.txt    # 安装依赖
```

### 创建数据库

默认用的是`Sqlite`，如果要使用`MySQL`或其他数据库请自行配置。

```
python manage.py makemigrations    # 创建迁移
python manage.py migrate    # 实例化数据库
```

### 创建管理用户

```
python manage.py createsuperuser    # 创建管理用户

Username (leave blank to use 'fnngj'): admin    # 管理员帐号
Email address: admin@mail.com      # email
Password:                          # 密码
Password (again):                  # 重复密码
Superuser created successfully.
```

### 运行

```
python manage.py runserver
```