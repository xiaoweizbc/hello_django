# 最简单的django demo

1.在命令提示符中输入
    cd 到一个存放目录的路径下
    django-admin startproject hello_django

2.编写hello_django/setting.py项目设置文件
    变量ALLOWED_HOSTS中加入"*"（允许除本地回环的所有主机ip来运行django项目）

3.编写hello_django/urls.py路由文件

4.新建并编写hello_django/views.py视图文件

5.在命令提示符中cd到项目的目录下
    python2 manage.py runserver (主机ip及端口号，如不填写着默认本地回环127.0.0.1:8000)

6.打开浏览器访问127.0.0.1:8000
