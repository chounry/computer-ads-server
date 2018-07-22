from dal import autocomplete

from .models import *
from cpu.models import Socket_type


class FormFactorAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
        #     return Form_factor.objects.none()

        qs = Form_factor.objects.all()

        if self.q:
            qs = qs.filter(name__startswith=self.q)
        return qs

class CompanyAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Company.objects.all()
        if self.q:
            qs = qs.filter(name__startswith=self.q)
        return qs

class SocketTypeAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Socket_type.objects.all()
        if self.q:
            qs = qs.filter(name__startswith=self.q)
        return qs
class ChipsetAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Chipset.objects.all()
        if self.q:
            qs = qs.filter(name__startswith=self.q)
        return qs


# Market