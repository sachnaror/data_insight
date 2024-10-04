from django.urls import path
from .views import upload_and_analyze_dataset, upload_dataset, dataset_list, analyze_dataset

urlpatterns = [
    path('upload/', upload_and_analyze_dataset, name='upload_and_analyze'),
    path('upload-dataset/', upload_dataset, name='upload_dataset'),  # Ensure other paths are correctly defined
    path('datasets/', dataset_list, name='dataset_list'),
    path('analyze/<int:dataset_id>/', analyze_dataset, name='analyze_dataset'),
]
