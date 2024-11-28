from django.urls import path
from . import views

app_name= 'templating'

urlpatterns=[
    path('',views.homepage, name='homepage')

]