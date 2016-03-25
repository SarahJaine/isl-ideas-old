from django.conf.urls import include, url
from django.contrib import admin
from . import views
from .views import IdeaList, IdeaDetail, IdeaCreate, IdeaUpdate
# from googleauth import login, callback, logout

urlpatterns = [

    url(r'^$', IdeaList.as_view(),
        name='home'),
    url(r'^idea/(?P<slug>[-\w]+)$', IdeaDetail.as_view(),
        name='idea_detail'),
    url(r'^new/$', IdeaCreate.as_view(),
        name='idea_form'),
    url(r'^idea/(?P<slug>[-\w]+)/edit/$', IdeaUpdate.as_view(),
        name='idea_edit'),

    # url(r'^auth/', include('googleauth.urls')),
    # url(r'^login/$', 'googleauth.views.login', name='googleauth_login'),
    # url(r'^callback/$', 'googleauth.views.callback', name='googleauth_callback'),
    # url(r'^logout/$', 'googleauth.views.logout', name='googleauth_logout'),
    url(r'^admin/', include(admin.site.urls)),
]
