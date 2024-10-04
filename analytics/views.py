from django.shortcuts import render, redirect, get_object_or_404
from .forms import DatasetUploadForm
from .models import Dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from faker import Faker
import os
from django.conf import settings

# Use a non-interactive backend for script usage
import matplotlib
matplotlib.use('Agg')

# Generate sample data using Faker (for testing)
def generate_sample_data():
    fake = Faker()
    data = {
        "name": [fake.name() for _ in range(100)],
        "age": [fake.random_int(min=18, max=80) for _ in range(100)],
        "salary": [fake.random_int(min=30000, max=120000) for _ in range(100)],
    }
    return pd.DataFrame(data)

def upload_dataset(request):
    if request.method == "POST":
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.user = request.user
            dataset.save()
            return redirect('dataset_list')  # Ensure this name matches your URL pattern
    else:
        form = DatasetUploadForm()
    return render(request, 'analytics/upload.html', {'form': form})

def dataset_list(request):
    datasets = Dataset.objects.filter(user=request.user)
    return render(request, 'analytics/dataset_list.html', {'datasets': datasets})

def analyze_dataset(request, dataset_id):
    dataset = get_object_or_404(Dataset, id=dataset_id)

    # Ensure file exists before proceeding
    if not os.path.exists(dataset.file.path):
        return render(request, 'analytics/analysis_result.html', {'error': 'File not found.'})

    df = pd.read_csv(dataset.file.path)

    # Example: Simple Linear Regression Analysis
    if 'age' in df.columns and 'salary' in df.columns:
        X = df[['age']]
        y = df['salary']
        model = LinearRegression()
        model.fit(X, y)
        predictions = model.predict(X)

        # Plotting
        plt.scatter(df['age'], df['salary'], color='blue', label='Data Points')
        plt.plot(df['age'], predictions, color='red', label='Regression Line')
        plt.title('Age vs Salary')
        plt.xlabel('Age')
        plt.ylabel('Salary')
        plt.legend()

        # Ensure the directory exists for saving the plot
        image_dir = os.path.join(settings.BASE_DIR, 'data_insight/staticfiles/analytics')
        os.makedirs(image_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Save the plot to the static directory
        image_path = os.path.join(image_dir, 'plot.png')
        plt.savefig(image_path)
        plt.close()  # Close the plot to free memory

        # Get the image path to pass to the template
        image_path_to_display = os.path.join('analytics', 'plot.png')  # Adjust path for template rendering

        return render(request, 'analytics/analysis_result.html', {'image_path': image_path_to_display})
    else:
        return render(request, 'analytics/analysis_result.html', {'error': 'Required columns not found in dataset.'})
