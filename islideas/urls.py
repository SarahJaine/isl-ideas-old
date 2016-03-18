from django.conf.urls import include, url
from django.contrib import admin
from . import views
from .views import IdeaList, IdeaDetail, IdeaCreate, IdeaUpdate, CommentCreate

urlpatterns = [

    url(r'^$', IdeaList.as_view(),
        name='home'),
    url(r'^idea/(?P<slug>[-\w]+)$', IdeaDetail.as_view(),
        name='idea_detail'),
    url(r'^new/$', IdeaCreate.as_view(),
        name='idea_form'),
    url(r'^idea/(?P<slug>[-\w]+)/edit/$', IdeaUpdate.as_view(),
        name='idea_edit'),
    url(r'^admin/', include(admin.site.urls)),
]
