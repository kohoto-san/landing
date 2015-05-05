from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import CreateView
from landing import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'landing.views.emails', name='landing'),
    #url(r'^$', views.EmailsView.as_view(), name="index"),
    url(r'^$', views.landing, name="index"),
    url(r'^subscribe$', views.form, name="subscribe"),
    url(r'^thanks/$', views.thanks, name="thanks"),


    #url(r'^about/$', views.about, name="about"),
)
