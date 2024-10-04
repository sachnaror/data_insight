# analytics/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_dataset, name='upload_dataset'),
    path('datasets/', views.dataset_list, name='dataset_list'),
    path('analyze/<int:dataset_id>/', views.analyze_dataset, name='analyze_dataset'),
]
