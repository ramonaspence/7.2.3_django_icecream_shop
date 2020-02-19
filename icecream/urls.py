from django.urls import path

from . import views


app_name = 'icecream'

urlpatterns = [
    path('icecream/', views.IndexView.as_view()),
    path('', views.IndexView.as_view(), name = 'index')
]
