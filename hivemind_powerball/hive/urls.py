from django.conf.urls import url

from .views import DroneCreate, DroneUpdate, DroneDelete
from .views import DroneDetail, DroneList


urlpatterns = [
    url(r'^drone/add/$',
        DroneCreate.as_view(), name='drone-add'),
    url(r'^drone/(?P<pk>[0-9]+)/edit/$',
        DroneUpdate.as_view(), name='drone-update'),
    url(r'^drone/(?P<pk>[0-9]+)/delete/$',
        DroneDelete.as_view(), name='drone-delete'),
    url(r'^drone/(?P<pk>[0-9]+)/$',
        DroneDetail.as_view(), name='drone-detail'),
    url(r'^drones/$',
        DroneList.as_view(), name='drone-list'),
]
