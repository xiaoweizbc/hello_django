from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),  # http://127.0.0.1:8000/hello/
]
