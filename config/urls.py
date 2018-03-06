from django.conf.urls import include, url
from django.contrib import admin

from orders.views import EasterEgg

urlpatterns = [
    url('grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include('orders.urls', namespace='orders')),
    url(r'^donald-trump/', EasterEgg.as_view(), name='donald_trump')
]
