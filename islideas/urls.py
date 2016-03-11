from django.conf.urls import include, url
from django.contrib import admin
from . import views
# from django.views.generic import TemplateView
# from .views import IndexView

urlpatterns = [
    # Examples:
    # url(r'^$', 'islideas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='home'),
    # url(r'^ideas/index/', IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
