# data_insight/urls.py

from django.contrib import admin
from django.urls import include, path

app_name = 'analytics'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analytics/', include('analytics.urls')),  # Include your analytics app URLs here
]
