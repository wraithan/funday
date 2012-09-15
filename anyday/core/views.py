from django.views.generic.detail import DetailView

from .models import Funday


class RandomFundayView(DetailView):
    model = Funday

    def get_object(self, *args, **kwargs):
        base_qs = self.get_queryset()

        if base_qs.exists():
            return base_qs[0]
        else:
            return None

    def get_queryset(self):
        return super(RandomFundayView, self).get_queryset().order_by('?')


class RaceRandomFundayView(RandomFundayView):
    def get_queryset(self):
        kwargs = {}

        if self.race in ['protoss', 'terran', 'zerg']:
            kwargs[self.race] = True

        return super(RaceRandomFundayView, self).get_queryset().filter(**kwargs)

    def get_template_names(self):
        return ['home.html']

    def get_context_data(self, *args, **kwargs):
        data = super(RaceRandomFundayView, self).get_context_data(*args, **kwargs)
        data['race'] = self.race
        return data

    def get(self, request, *args, **kwargs):
        self.race = kwargs.get('race', 'protoss')
        return super(RaceRandomFundayView, self).get(request, *args, **kwargs)
