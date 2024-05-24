from django.urls import path
from . import views


urlpatterns = [
    path('', views.find_jobs, name='find_jobs'),
    path('skills_form/', views.skills_form, name='skills_form'),
]