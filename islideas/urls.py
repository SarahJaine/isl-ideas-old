from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import RedirectView
from .views import IdeaList, IdeaDetail, IdeaCreate, IdeaUpdate, IdeaDelete, CommentDelete

urlpatterns = [

    url(r'^$', IdeaList.as_view(),
        name='home'),
    url(r'^idea/(?P<slug>[-\w]+)$', IdeaDetail.as_view(),
        name='idea_detail'),
    url(r'^new/$', IdeaCreate.as_view(),
        name='idea_form'),
    url(r'^idea/(?P<slug>[-\w]+)/edit/$', IdeaUpdate.as_view(),
        name='idea_edit'),
    url(r'^idea/(?P<slug>[-\w]+)/delete/$', IdeaDelete.as_view(),
        name='idea_confirm_delete'),
    url(r'^idea/(?P<idea_slug>[-\w]+)/commmentdelete/(?P<pk>[-\w]+)/$',
        CommentDelete.as_view(),
        name='comment_confirm_delete'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('googleauth.urls')),
    url(r'^.*', RedirectView.as_view(pattern_name='home', permanent=True)),

]
