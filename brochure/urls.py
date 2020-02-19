from django.urls import path

from . import views

app_name = 'brochure'

urlpatterns = [
    path('', views.IndexView.as_view(), name='base'),
    path('icecream/', views.IndexView.as_view(), name='index')
]
