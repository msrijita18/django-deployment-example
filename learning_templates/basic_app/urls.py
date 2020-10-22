from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from basic_app import views

# Template tagging
## GLobal name
app_name = 'basic_app'

urlpatterns = [
    path("", views.index, name="index"),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),

]
