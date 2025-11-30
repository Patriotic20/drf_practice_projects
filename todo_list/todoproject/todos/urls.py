from django.urls import path
from todos import views

urlpatterns = [
    path('todos/', views.todo_list, name='todo-list'),
    path('todos/<int:pk>/', views.todo_detail, name='todo-detail'),
]