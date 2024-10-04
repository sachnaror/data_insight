# Django Data Analysis App

This Django application allows users to upload datasets, perform data analysis using AI techniques, and visualize the results through interactive plots. It also includes functionality for generating sample datasets using Faker.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- Upload CSV datasets and analyze them.
- Generate sample datasets using Faker for testing and development.
- Perform linear regression analysis and visualize the results with Matplotlib.
- Display summary statistics and correlation matrices for the uploaded datasets.
- User authentication for personalized data management.

## Installation

Follow these steps to set up the application on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/django-data-analysis-app.git
   cd django-data-analysis-app



```
├── data_insight/
│   ├── requirements.txt
│   ├── db.sqlite3
│   ├── README.md
│   ├── .env
│   ├── manage.py
│   ├── test_data.csv
│   ├── datasets/
│   │   ├── test_data_I6GYhmi.csv
│   │   ├── test_data_pnuMTwn.csv
│   │   ├── fake_user_data.csv

│   ├── data_insight/
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │   ├── staticfiles/
│   │   │   ├── analytics/
│   │   │   │   ├── plot.png
│   │   │   │   └── regression_plot.png
│   ├── staticfiles/
│   │   └── plot.png
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── images/
│   │   │   └── logo.png
│   │   ├── js/
│   │   │   └── script.js
│   │   ├── admin/
│   │   │   ├── css/
│   │   │   ├── js/
│   │   │   ├── img/
│   │   ├── analytics/
│   │   │   └── plot.png
│   ├── static/
│   │   └── plot.png
│   │   ├── analytics/
│   │   │   └── plot.png
│   ├── analytics/
│   │   ├── models.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │   ├── management/
│   │   │   ├── commands/
│   │   │   │   └── generate_fake_data.py
│   │   ├── static/
│   │   │   └── plot.png
│   │   │   ├── css/
│   │   │   │   └── style.css
│   │   │   ├── images/
│   │   │   │   └── logo.png
│   │   │   ├── js/
│   │   │   │   └── script.js
│   │   ├── templates/
│   │   │   └── base.html
│   │   │   ├── analytics/
│   │   │   │   ├── home.html
│   │   │   │   ├── dataset_list.html
│   │   │   │   ├── analysis_result.html
│   │   │   │   └── upload.html
