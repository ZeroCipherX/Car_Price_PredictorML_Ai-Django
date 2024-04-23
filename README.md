# Car_Price_PredictorML_Ai-Django
Car Price Predictor: A Django web app utilizing AI linear regression to estimate the selling price of used cars based on key features.
```
Car_Price_PredictorML_Ai-Django/
│
├── carwebapp/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── main/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── images/
│   │   │   ├── image.jpg
│   │   │   └── image2.jpeg
│   │   ├── video/
│   │   │   └── particles.mp4
│   │   └── js/
│   │       ├── script.js
│   │       ├── clock.js
│   │       └── smokeEffect.js
│   └── templates/
│       └── views/
│           ├── index.html
│           └── predict.html
│
└── model/
    ├── Cleaned_Car_data.csv
    ├── LinearRegressionModel.pkl
    └── joblib.ipynb
```
---

# Car Price Predictor ML AI-Django

## Overview
Car Price Predictor ML AI-Django is a web application built on Django framework that utilizes machine learning to predict the selling price of used cars. The application employs linear regression to estimate the price based on various features such as mileage, model, year, brand, and transmission.

## Project Structure

### carwebapp/
This directory contains the main project configuration files for Django.

- **__init__.py**: Marks the directory as a Python package.
- **settings.py**: Settings/configuration for the Django project.
- **urls.py**: URL declarations for the project.
- **wsgi.py**: Entry-point for WSGI-compatible web servers to serve the project.

### main/
This directory is the Django app directory where the main functionality of the project resides.

- **migrations/**: Directory containing database migration files.
- **__init__.py**: Package initializer.
- **admin.py**: Configuration for Django admin panel.
- **models.py**: Defines data models for the app.
- **urls.py**: URL configurations for the app.
- **views.py**: Contains view functions for handling HTTP requests.
- **static/**: Directory for storing static files.
  - **css/**: CSS stylesheets.
  - **images/**: Image files used in the app.
  - **video/**: Video files.
  - **js/**: JavaScript files.
- **templates/**: Directory for HTML templates.
  - **views/**: Templates specific to the main app.
    - **index.html**: Homepage template.
    - **predict.html**: Template for displaying price predictions.

### model/
This directory contains the machine learning model and data files.

- **Cleaned_Car_data.csv**: Dataset containing cleaned car data used for training the model.
- **LinearRegressionModel.pkl**: Pickle file containing the trained linear regression model.
- **Jupyternotebook.ipynb**: Jupyter notebook containing code for data preprocessing, model training, and evaluation.

## Usage
1. Install Python and Django.
2. Clone the repository.
3. Navigate to the project directory.
4. Install dependencies using `pip install -r requirements.txt`.
5. Run migrations: `python manage.py migrate`.
6. Start the development server: `python manage.py runserver`.
7. Access the web application in your browser at the specified URL.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

