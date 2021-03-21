from django.conf.urls import url
from django.contrib import admin


from .views import(
	posts_list,
	posts_detail,
	
	)

urlpatterns = [
 	url(r'^$', posts_list, name='blog'),
    url(r'^(?P<id>\d+)/$', posts_detail, name="detail"),

]
