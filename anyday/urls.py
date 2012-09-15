from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api

from core.api.resources import FundayResource
from core.views import RandomFundayView


admin.autodiscover()

v1_api = Api()
v1_api.register(FundayResource())

urlpatterns = patterns(
    '',  # View prefix
    url(r'^$',
        RandomFundayView.as_view(template_name='home.html'),
        name='home'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
