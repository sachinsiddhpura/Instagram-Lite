from django.urls import path,re_path
from .views import PostUpdate,PostCreate,PostDelete,PostList,PostDetail
from django.views.generic.base import RedirectView
app_name = 'posts'

urlpatterns =[
    re_path(r'^$', RedirectView.as_view(url="/")), 
    path('search/', PostList.as_view(), name='list'),
    path('create/', PostCreate.as_view(), name='create'), 
    re_path(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='detail'),
    re_path(r'^(?P<pk>\d+)/update/$', PostUpdate.as_view(), name='update'), 
    re_path(r'^(?P<pk>\d+)/delete/$', PostDelete.as_view(), name='delete'), 
]