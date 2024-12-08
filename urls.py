from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='Home'),
    path('blog/',views.blog,name='Blog'),
    path('feature/',views.feature,name='Feature'),
    path('about/',views.about,name='About'),
    path('contact/',views.contact,name='Contact'),
    path('services/',views.services,name='Services'),
    path('team/',views.team,name='Team'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('appointment/',views.appointment,name='appointment'),



]