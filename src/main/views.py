from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main_view(request):
  
    return render(request, "views/index.html")

def predict(request):
    return render(request, 'views/predict.html')

def result(request):
    # Load and clean data
    car = pd.read_csv('/home/cyber/Desktop/Project/src/model/Cleaned_Car_data.csv')
    car.drop(['Unnamed: 0', 'Version'], axis=1, inplace=True)

    # Separating features and target
    X = car.drop('Price', axis=1)
    Y = car['Price'] * 0.95  # Adjust target prices to be 5% less

    # Model initialization and training
    model = LinearRegression()
    X_encoded = pd.get_dummies(X)
    model.fit(X_encoded, Y)

    # Extract request values
    user_data = {
        'Make': [request.GET.get('make')],
        'Model': [request.GET.get('model')],
        'Make_Year': [int(request.GET.get('make_year'))],
        'CC': [int(request.GET.get('cc'))],
        'Assembly': [request.GET.get('assembly')],
        'Mileage': [int(request.GET.get('mileage'))],
        'Registered_City': [request.GET.get('registered_city')],
        'Transmission': [request.GET.get('transmission')]
    }

    # Creating the DataFrame for input data
    input_data = pd.DataFrame(user_data)
    input_data_encoded = pd.get_dummies(input_data)
    input_data_encoded = input_data_encoded.reindex(columns=X_encoded.columns, fill_value=0)

    # Make prediction
    predicted_price = model.predict(input_data_encoded)
    predicted_price_adjusted = round(predicted_price[0])

    # Render the result
    price_message = f"The predicted price is Rs: {predicted_price_adjusted}"
    return render(request, "views/predict.html", {"result2": price_message})
