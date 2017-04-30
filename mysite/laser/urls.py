from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^(?P<category_id>[0-9]+)/$', category_view, name = "category_view"),
    url(r'^(?P<category_id>[0-9]+)/(?P<subcategory_id>[0-9]+)/$', subcategory_view, name = "subcategory_view"),
    url(r'^(?P<category_id>[0-9]+)/(?P<subcategory_id>[0-9]+)/(?P<item_id>[0-9]+)$', item_view, name = "item_view"),
    url(r'^all_news/$', all_news, name="all_news"),
    url(r'^newsarticle_view/(?P<newsarticle_id>[0-9]+)/$', newsarticle_view, name="newsarticle_view"),    
    url(r'^new_items/$', new_items, name="new_items"),    
]
