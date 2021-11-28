from os import name
from django.urls import path,include
from . import views


urlpatterns = [
    
    path("",views.indexPage,name='index'),
    path('our-services/',views.AllServices,name='our-services'),
    path("service-category/<int:serviceID>/",views.serviesCategory,name='servies-category'),
    path('service-detail/<int:serviceID>/',views.SeriviceDetail,name='service-detail')
]