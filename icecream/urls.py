from django.urls import path

from . import views


app_name = 'icecream'

urlpatterns = [
    # create path for add
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/edit/', views.UpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('add/', views.CreateView.as_view(), name='add'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('<str:selection>/', views.IndexView.as_view(), name ='selection'),

]

##use <int:pk> in urls when allows it to target a specific primary key (pk)
