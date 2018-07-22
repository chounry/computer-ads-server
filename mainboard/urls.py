from django.urls import path
from . import views
from . import autocomplete_views

app_name= 'mainboard'

urlpatterns = [
    path('',views.get_all_moth,name = 'all_mainboards'),
    path('mainboard/<slug:slug>/', views.get_moth_detail, name='mainboard_detail'),
    path('form/mainboard/',views.handle_form, name='mainboard_form'),

    # for auto-complete
    path('form/mainboard/form-factor-ac/', autocomplete_views.FormFactorAC.as_view(create_field='name') , name='form-factor-ac'),
    path('form/mainboard/company-ac/',autocomplete_views.CompanyAC.as_view(create_field='name'), name='company-ac'),
    path('form/mainboard/socket-type-ac/',autocomplete_views.SocketTypeAC.as_view(create_field='name'), name='socket-type-ac'),
    path('form/mainboard/chipset-ac/',autocomplete_views.ChipsetAC.as_view(create_field='name'), name='chipset-ac'),
    
]