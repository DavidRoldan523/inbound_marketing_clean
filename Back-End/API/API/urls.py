from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #Apps
    url(r'^api/v1/transform/', include('inboud_transform.urls')),
    url(r'^admin/', admin.site.urls)
]
