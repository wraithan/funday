from django.conf.urls.defaults import url
from tastypie.resources import ModelResource, ALL
from tastypie.serializers import Serializer
from ..models import Funday


class FundayResource(ModelResource):
    class Meta(object):
        queryset = Funday.objects.all()
        allowed_methods = ['get']
        filtering = {
            'protoss': ALL,
            'zerg': ALL,
            'terran': ALL,
            'game_type': ALL,
        }
        # Only ever JSON.
        serializer = Serializer(formats=['json'])

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/random/$" % self._meta.resource_name, self.wrap_view('get_random'), name="api_get_random"),
        ]

    def get_random(self, request, **kwargs):
        # This lets the ``filtering`` bits continue to work on this endpoint.
        applicable_filters = self.build_filters(filters=request.GET)
        object_list = self.apply_filters(request, applicable_filters)

        # Order by random & yank off the last one.
        random = object_list.order_by('?')[0]

        # Normal Tastypie GET detail calls follow.
        bundle = self.build_bundle(obj=random, request=request)
        bundle = self.full_dehydrate(bundle)
        return self.create_response(request, bundle)
