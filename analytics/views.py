from django.shortcuts import render, redirect, get_object_or_404
from .forms import DatasetUploadForm, UploadFileForm
from .models import Dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from faker import Faker
import os
from django.conf import settings
import logging

# Use a non-interactive backend for script usage
import matplotlib
matplotlib.use('Agg')

# Set up logging
logger = logging.getLogger(__name__)

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
    """Handle the uploading of datasets."""
    if request.method == "POST":
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.user = request.user
            dataset.save()
            logger.info("Dataset uploaded: %s", dataset.file.name)  # Log dataset upload
            return redirect('analytics:dataset_list')  # Ensure this matches your URL pattern
    else:
        form = DatasetUploadForm()

    return render(request, 'analytics/upload.html', {'form': form})

def dataset_list(request):
    """Display the list of uploaded datasets."""
    datasets = Dataset.objects.filter(user=request.user)
    return render(request, 'analytics/dataset_list.html', {'datasets': datasets})

def analyze_dataset(request, dataset_id):
    """Analyze the uploaded dataset."""
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

def analyze_view(request):
    """Analyze the uploaded CSV file from a different upload form."""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            logger.info("CSV file uploaded: %s", csv_file.name)  # Log uploaded file name

            # Process the uploaded CSV
            df = pd.read_csv(csv_file)
            logger.info("CSV data: %s", df.head())  # Log the first few rows of the data

            # Perform analysis on df here
            analysis_results = perform_analysis(df)  # Define this function according to your analysis needs

            return render(request, 'analytics/result.html', {'analysis_results': analysis_results})
    else:
        form = UploadFileForm()

    return render(request, 'analytics/upload.html', {'form': form})

def upload_and_analyze_dataset(request):
    """Upload and immediately analyze the dataset."""
    if request.method == 'POST':
        form = DatasetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.user = request.user
            dataset.save()

            # Proceed with analysis
            df = pd.read_csv(dataset.file.path)
            analysis_results = perform_analysis(df)  # Call perform_analysis function

            return render(request, 'analytics/analysis_result.html', {'analysis_results': analysis_results})
    else:
        form = DatasetUploadForm()

    return render(request, 'analytics/upload.html', {'form': form})

def perform_analysis(df):
    """Perform analysis on the given DataFrame and return the results."""
    try:
        # Check if the required columns exist for regression analysis
        if 'age' in df.columns and 'salary' in df.columns:
            # Perform Linear Regression (Age vs Salary as an example)
            X = df[['age']]
            y = df['salary']
            model = LinearRegression()
            model.fit(X, y)
            predictions = model.predict(X)

            # Calculate the regression score (R^2)
            regression_score = model.score(X, y)

            # Plot the regression line and data points
            plt.scatter(df['age'], df['salary'], color='blue', label='Data Points')
            plt.plot(df['age'], predictions, color='red', label='Regression Line')
            plt.title('Age vs Salary Regression')
            plt.xlabel('Age')
            plt.ylabel('Salary')
            plt.legend()

            # Ensure the directory exists for saving the plot
            image_dir = os.path.join(settings.BASE_DIR, 'data_insight/staticfiles/analytics')
            os.makedirs(image_dir, exist_ok=True)

            # Save the plot
            image_path = os.path.join(image_dir, 'regression_plot.png')
            plt.savefig(image_path)
            plt.close()  # Close the plot to free memory

            # Convert image path for template usage
            regression_image_path = os.path.join('analytics', 'regression_plot.png')
        else:
            regression_score = None
            regression_image_path = None

        # Correlation matrix
        correlation_matrix = df.corr()

        # Example: You can also include correlation coefficients for specific pairs
        if 'age' in df.columns and 'salary' in df.columns:
            age_salary_correlation = df['age'].corr(df['salary'])
        else:
            age_salary_correlation = None

        # Summary statistics
        description = df.describe()  # Get summary statistics
        column_names = df.columns.tolist()  # Get list of columns
        head = df.head()  # Get the first few rows of the dataset

        # Prepare the results in a format you want to pass to the template
        analysis_results = {
            'description': description.to_html(),  # Convert DataFrame to HTML for display
            'column_names': column_names,
            'head': head.to_html(),
            'correlation_matrix': correlation_matrix.to_html(),  # Correlation matrix as HTML
            'age_salary_correlation': age_salary_correlation,  # Correlation between age and salary
            'regression_score': regression_score,  # R^2 score for regression
            'regression_image_path': regression_image_path  # Path to regression plot image
        }

        return analysis_results

    except Exception as e:
        logger.error("Error during analysis: %s", str(e))
        return {'error': 'Analysis failed due to an error.'}

def home_view(request):
    """Render the home page."""
    return render(request, 'analytics/home.html')
