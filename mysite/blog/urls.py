from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/edit/(?P<pk>\d+)/$', views.post_edit, name='post_edit'),
    url(r'^post/publish/(?P<pk>\d+)/$', views.post_publish, name='post_publish'),
    url(r'^post/unpublish/(?P<pk>\d+)/$', views.post_unpublish, name='post_unpublish'),
    url(r'^post/delete/(?P<pk>\d+)/$', views.post_delete, name='post_delete'),
]