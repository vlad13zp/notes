"""
note URL Configuration
"""
from django.conf.urls import url
from note import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^signup/$', views.SignUp.as_view(), name='sign_up'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^delete/(\d+)$', views.delete, name='delete'),
    url(r'^edit/(?P<pk>\d+)$', views.EditView.as_view(), name='edit'),
    url(r'^cat/(?P<pk>\d+)$', views.CatView.as_view(), name='cat'),
]
