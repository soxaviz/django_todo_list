from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:pk>', views.category_view, name='category'),
    path('todo/<int:pk>/', views.todo_list, name='todo_detail'),


]


