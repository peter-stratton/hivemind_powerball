from django.conf.urls import url

from .views import new_ticket


urlpatterns = [
    url(r'^add/$', new_ticket, name='ticket-add'),
]
