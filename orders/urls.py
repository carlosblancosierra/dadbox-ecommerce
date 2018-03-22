from django.conf.urls import url

from .views import (
    OrderListView,
    OrderDetailView,
    ReferredOrderListView
    )

urlpatterns = [
    url(r'^$', OrderListView.as_view(), name='list'),
    url(r'^ref/$', ReferredOrderListView.as_view(), name='ref'),
    url(r'^(?P<order_id>[0-9A-Za-z]+)/$', OrderDetailView.as_view(), name='detail'),
]
