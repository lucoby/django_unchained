from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.ThreadView.as_view(), name='thread'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]