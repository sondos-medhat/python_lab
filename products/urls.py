from django.urls import path
from django.conf.urls import url
# from . import view
from .views import home,item
urlpatterns = [
    path('home',home.index),
    path('item', item.index,name='item_list'),
    url(r'^item/(?P<item_id>\d+)/$', item.read, name='item_read'),
    # path('item/add', item.add,name='item_add'),
    # path('item/save', item.save, name='item_save'),
    path('item/add', item.create, name='item_add'),
    url(r'^item/(?P<item_id>\d+)/delete$', item.delete, name='item_delete'),
    url(r'^item/(?P<item_id>\d+)/edit$', item.edit, name='item_edit'),
    url(r'^item/(?P<dept_id>\d+)/filter', item.filter, name='item_filter'),

]
