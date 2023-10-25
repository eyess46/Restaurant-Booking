from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('donate', views.donate, name='donate'),
    path('inner_page', views.inner_page, name='inner_page'),
    

]