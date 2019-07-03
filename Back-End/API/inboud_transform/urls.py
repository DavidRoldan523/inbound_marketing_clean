# SENTIMENT
from django.conf.urls import url
from .views import service_view

urlpatterns = [
    url(
        r'',
        service_view.service,
        name='service'
    )
]