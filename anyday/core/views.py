from django.views.generic.detail import DetailView

from .models import Funday


class RandomFundayView(DetailView):
    model = Funday

    def get_object(*args, **kwargs):
        if Funday.objects.exists():
            return Funday.objects.all().order_by('?')[0]
        else:
            return None
