from django.urls import path

from manage_todo.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create/', CreateTodo.as_view(), name='todo-create'),
    path('update/<int:pk>/', UpdateTodo.as_view(), name='todo-update'),
    path('delete/<int:pk>/', DeleteTodo.as_view(), name='todo-delete'),
    path('complete/<int:pk>/', CompleteToggle.as_view(), name='todo-complete-toggle'),
]
