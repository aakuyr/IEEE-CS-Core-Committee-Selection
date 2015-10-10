from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','home.views.index'),
    url(r'^junior/([0-9]{2})/([A-Z]{3})/([0-9]{4})/$','junior.views.index'),
    url(r'^junior/','junior.views.index'),
    url(r'^juniors/','QP.views.index'),
)