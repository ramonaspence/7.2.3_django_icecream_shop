from django.urls import path

from . import views


app_name = 'icecream'

urlpatterns = [
    # create path for add
    # path('icecream/', views.ListView.as_view(), name = 'index'),
    path('<str:selection>', views.IndexView.as_view(), name ='selection'),
    path('', views.IndexView.as_view(), name = 'index')
]

##use <int:pk> in urls when allows it to target a specific primary key (pk)
