from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.views.generic import TemplateView, ListView, DetailView
# from .views import IndexView

urlpatterns = [
    # Examples:
    # url(r'^$', 'islideas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='home'),
    url(r'^idea/(?P<slug>[-\w]+)/$', views.idea_detail,
        name='idea_detail'),
    # url(r'^ideas/$',
    #     TemplateView.as_view(template_name='ideas/ideas.html'),
    #     name='ideas'),
    url(r'^admin/', include(admin.site.urls)),
]
