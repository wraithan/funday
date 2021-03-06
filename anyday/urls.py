from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api

from core.api.resources import FundayResource
from core.views import FundayView, RaceRandomFundayView, RandomFundayView


admin.autodiscover()

v1_api = Api()
v1_api.register(FundayResource())

urlpatterns = patterns(
    '',  # View prefix
    url(r'^$',
        RandomFundayView.as_view(),
        name='home'),
    url(r'^funday/(?P<pk>\d+)/$',
        FundayView.as_view(),
        name='funday'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('webmaster_verification.urls')),
    url(r'^(?P<race>\w+)/$',
        RaceRandomFundayView.as_view(),
        name='random_race'),
)
