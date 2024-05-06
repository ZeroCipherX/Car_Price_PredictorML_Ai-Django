from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def main_view(request):
    return render(request, "views/index.html")

def predict(request):
    # Load the CSV file
    car = pd.read_csv('/home/cyber/Desktop/Project/src/model/Cleaned_Car_data.csv')

    # Get unique values for each column and sort them
    make_choices = sorted(car['Make'].unique())
    model_choices = sorted(car['Model'].unique())
    make_year_choices = sorted(car['Make_Year'].unique())
    cc_choices = sorted(car['CC'].unique())
    assembly_choices = sorted(car['Assembly'].unique())
    mileage_choices = sorted(car['Mileage'].unique())
    registered_city_choices = sorted(car['Registered_City'].unique())
    transmission_choices = sorted(car['Transmission'].unique())

    # Pass choices to the template
    context = {
        'make_choices': make_choices,
        'model_choices': model_choices,
        'make_year_choices': make_year_choices,
        'cc_choices': cc_choices,
        'assembly_choices': assembly_choices,
        'mileage_choices': mileage_choices,
        'registered_city_choices': registered_city_choices,
        'transmission_choices': transmission_choices
    }

    return render(request, "views/predict.html", context)

def result(request):
    if request.method == 'GET':
        # Load and clean data
        car = pd.read_csv('/home/cyber/Desktop/Project/src/model/Cleaned_Car_data.csv')

        car.drop(['Unnamed: 0', 'Version'], axis=1, inplace=True)

        # Separating features and target
        X = car.drop('Price', axis=1)
        Y = car['Price'] * 0.85  # Adjust target prices to be 15% less

        # Model initialization and training
        model = LinearRegression()
        X_encoded = pd.get_dummies(X)
        model.fit(X_encoded, Y)

        # Extract request values
        user_data = {
            'Make': [request.GET.get('make')],
            'Model': [request.GET.get('model')],
            'Make_Year': [int(request.GET.get('make_year', 0))],
            'CC': [int(request.GET.get('cc', 0))],
            'Assembly': [request.GET.get('assembly')],
            'Mileage': [int(request.GET.get('mileage', 0))],
            'Registered_City': [request.GET.get('registered_city')],
            'Transmission': [request.GET.get('transmission')]
        }

        # Basic form validation
        if '' in user_data.values() or 0 in [user_data['Make'][0], user_data['Model'][0], user_data['Make_Year'][0], user_data['CC'][0], user_data['Assembly'][0], user_data['Mileage'][0], user_data['Registered_City'][0], user_data['Transmission'][0]]:
            error_message = "Please fill in all fields with valid data."
            return render(request, "views/predict.html", {"error_message": error_message})

        # Creating the DataFrame for input data
        input_data = pd.DataFrame(user_data)
        input_data_encoded = pd.get_dummies(input_data)
        
        # Align the columns of input_data_encoded and X_encoded
        input_data_encoded = input_data_encoded.reindex(columns=X_encoded.columns, fill_value=0)

        # Make multiple predictions
        num_predictions = 5
        predicted_prices = []
        for _ in range(num_predictions):
            predicted_price = model.predict(input_data_encoded)
            predicted_prices.append(predicted_price)

        # Calculate the mean of predicted prices
        predicted_price_mean = round(np.mean(predicted_prices))

        # Render the result
        price_message = f"The predicted price is Rs: {predicted_price_mean}"
        return render(request, "views/predict.html", {"result2": price_message})

    # If request method is not GET
    return render(request, "views/predict.html")
