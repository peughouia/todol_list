from django.contrib import admin
from django.urls import path
import tasks.views as views

urlpatterns = [
    path('', views.index, name="home"),
    path('add_collection/', views.add_collection, name="add_collection"),
    path('add_task/', views.add_task, name="add_task"),
    path('delete_task/<int:task_pk>', views.delete_task, name="delete_task"),
    path('delete_collection/<int:collection_pk>', views.delete_collection, name="delete_collection"),
    path('get_tasks/<int:collection_pk>/', views.get_tasks, name="get_tasks"),
    path('admin/', admin.site.urls),
]
