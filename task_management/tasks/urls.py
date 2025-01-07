from django.urls import path
from . import views
from .views import TaskDeleteView
from django.shortcuts import redirect

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('logout/', views.user_logout, name='user_logout'),
    path('home/', lambda request: redirect('task_list'), name='home'),  # Add this
    path('task/search/', views.task_search, name='task_search'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]
