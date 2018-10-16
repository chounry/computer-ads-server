from dal import autocomplete

from .models import *
from cpu.models import Socket_type


class CPUModelAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Form_factor.objects.none()

        qs = CPU_model.objects.all()

        if self.q:
            qs = qs.filter(name__startswith=self.q)
        return qs

class VerticalSegmentAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Vertical_segment.objects.all()
        if self.q:
            qs = qs.filter(name__startswith=self.q)
        return qs

class SocketTypeAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Socket_type.objects.all()
        if self.q:
            qs = qs.filter(name__startswith=self.q)
        return qs
        
class SeriesAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Series.objects.all()
        if self.q:
            qs = qs.filter(name__startswith=self.q)
        return qs

class CPUBrandAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = CPU_brand.objects.all()
        if self.q:
            qs = qs.filter(name__startswith=self.q)
        return qs

class CPUNumOfCoreAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Num_of_core.objects.all()
        if self.q:
            qs = qs.filter(name__startswith=self.q)
        return qs
# Market