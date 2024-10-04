from django import forms
from .models import Dataset  # Ensure you have the correct import

class DatasetUploadForm(forms.ModelForm):
    class Meta:
        model = Dataset  # Use your actual model name
        fields = ['file']  # Adjust fields according to your Dataset model

class UploadFileForm(forms.Form):
    file = forms.FileField()  # Simple file upload form


