import joblib
model=joblib.load("Car_price_predictor.pkl")
def get_car_price_prediction(car_age_in_months):
    try:
        car_age_in_months=int(car_age_in_months)
        car_price=model.predict([[car_age_in_months]])
        return car_price[0]
    except ValueError:
        raise Exception("Please enter a valid number")
    
    