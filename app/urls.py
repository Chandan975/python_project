from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoViewSet.as_view({'get': 'list', 'post': 'create'}), name='todo-list'),
    path('todos/<int:pk>/', views.TodoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='todo-detail'),
    path('users/', views.UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('users/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
]
