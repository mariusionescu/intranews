from django.conf.urls import include, url
from django.contrib import admin
import wall

admin.site.site_header = 'IntraNews'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^wall/', include(wall.urls))
]
