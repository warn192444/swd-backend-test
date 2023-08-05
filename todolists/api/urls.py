from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTodoLists),
    path('add-todo/', views.addTodoList),
    path('update/<int:pk>/', views.updateTodoList, name='update_todo'),
]