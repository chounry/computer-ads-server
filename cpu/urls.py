from django.urls import path
from . import autocomplete_views
from . import views

app_name = "cpu"

urlpatterns = [
    path("", views.get_all_cpu, name="all_cpu"),
    path("<slug:slug>/", views.get_cpu_detail, name="cpu_detail"),

    path('form/cpu/',views.handle_form,name='cpu_form'),
    path('form/cpu/cpu-model-ac/', autocomplete_views.CPUModelAC.as_view(create_field='name') , name='cpu_model-ac'),
    path('form/cpu/cpu-brand-ac/',autocomplete_views.CPUBrandAC.as_view(create_field='name'), name='cpu_brand-ac'),
    path('form/cpu/socket-type-ac/',autocomplete_views.SocketTypeAC.as_view(create_field='name'), name='socket-type-ac'),
    path('form/cpu/vertical-segment-ac/',autocomplete_views.VerticalSegmentAC.as_view(create_field='name'), name='vertical_segment-ac'),
    path('form/cpu/series-ac/',autocomplete_views.SeriesAC.as_view(create_field='name'), name='series-ac'),
    path('form/cpu/num-of-cores-ac/',autocomplete_views.SeriesAC.as_view(create_field='name'), name='num-of-cores-ac'),
]