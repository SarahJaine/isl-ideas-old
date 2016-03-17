from django.conf.urls import include, url
from django.contrib import admin
from . import views
from .views import IdeaList

urlpatterns = [

    url(r'^$', IdeaList.as_view(), name='home'),

    url(r'^idea/(?P<slug>[-\w]+)/$', views.idea_detail,
        name='idea_detail'),
    url(r'^idea/(?P<slug>[-\w]+)/edit/$', views.edit_idea,
        name='edit_idea'),
    url(r'^new/$', views.new_idea, name='new_idea'),

    url(r'^admin/', include(admin.site.urls)),
]
