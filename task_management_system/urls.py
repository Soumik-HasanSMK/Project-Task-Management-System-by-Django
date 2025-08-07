from django.contrib import admin
from django.urls import path
from tasks import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task_list, name='task_list'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/update/<int:pk>/', views.update_task, name='update_task'),
    path('task/delete/<int:pk>/', views.delete_task, name='delete_task'),
]
