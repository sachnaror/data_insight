# data_insight/analytics/urls.py

from django.urls import path
from .views import upload_dataset, dataset_list, analyze_dataset

urlpatterns = [
    path('upload/', upload_dataset, name='upload_dataset'),
    path('datasets/', dataset_list, name='dataset_list'),
    path('analyze/<int:dataset_id>/', analyze_dataset, name='analyze_dataset'),
]
