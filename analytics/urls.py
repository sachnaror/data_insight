from django.urls import path
from .views import upload_and_analyze_dataset, upload_dataset, dataset_list, analyze_dataset
from . import views

app_name = 'analytics'  # Namespace for this app's URLs

urlpatterns = [
    path('', views.home_view, name='home'),  # Home view
    path('upload/', upload_and_analyze_dataset, name='upload_and_analyze'),  # Upload and analyze
    path('upload-dataset/', upload_dataset, name='upload_dataset'),  # Upload dataset
    path('datasets/', dataset_list, name='dataset_list'),  # List of datasets
    path('analyze/<int:dataset_id>/', analyze_dataset, name='analyze_dataset'),  # Analyze a specific dataset
]
