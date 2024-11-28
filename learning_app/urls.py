from django.urls import path
from . import views
# from .views import our_story, our_team_members, contact_us

urlpatterns = [
    path('home/', views.home,name='home'),
    path('our-story/', views.our_story, name='our_story'),
    path('our-team-members/', views.our_team_members, name='our_team_members'),
    path('contact-us/', views.contact_us, name='contact_us'),
]