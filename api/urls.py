from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^information/$',views.update_information,name='information'),
    url(r'^information1/$',views.update_information1,name='information1'),
    url(r'^information2/$',views.update_information2,name='information2'),
    url(r'^information3/$',views.update_information3,name='information3'),
    
]
