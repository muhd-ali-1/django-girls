from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as authViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', authViews.login, name='login'),
    url(r'^accounts/logout/$', authViews.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
    # url(r'^accounts/', include('allauth.urls')),
]
