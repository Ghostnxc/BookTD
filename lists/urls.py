
from django.conf.urls import include, url
from lists import views as list_viewss
from lists import urls as list_urls

urlpatterns = [
    url(r'^new$', views.list_viewss.new_list, name='new_list'),
     url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
    url(r'^lists/new$', views.new_list, name='new_list'),
    url(r'^lists/the-only-list-in-the-world/$', views.view_list, name='view_list'),
    url(r'^lists/(.+)/$', views.view_list, name='view_list'),
    url(r'^lists/(\d+)/$', views.view_list, name='view_list'),
]
