from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^number/$', views.get_composite_ticket),
	url(r'', views.main_view),
]
