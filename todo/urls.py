from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('task-detail/', views.task_detail, name='task_detail'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'), 
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),  # Corrected URL for edit_task
]
