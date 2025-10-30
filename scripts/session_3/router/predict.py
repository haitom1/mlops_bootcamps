import mlflow.sklearn
import pandas as pd
from fastapi import APIRouter

from scripts.session_3.scripts.Prediction_request import PredictRequest
from scripts.session_3.scripts.Prediction_Response import PredictResponse

mlflow.set_tracking_uri("http://localhost:8080")

model_name = "housing_price_predictor"
model_version = "2"

model_uri = f"models:/{model_name}/{model_version}"

model = mlflow.sklearn.load_model(model_uri)

housing_router = APIRouter(prefix="/housing")

@housing_router.post("/predict", response_model=PredictResponse)
def predict_housing_router(request: PredictRequest):
    input_data = {
        "Avg. Area Income": [request.Avg_Area_Income],
        "Avg. Area House Age": [request.Avg_Area_House_Age],
        "Avg. Area Number of Rooms": [request.Avg_Area_Number_of_Rooms],
        "Avg. Area Number of Bedrooms": [request.Avg_Area_Number_of_Bedrooms],
        "Area Population": [request.Area_Population],
    }
    input_data = pd.DataFrame(input_data)
    prediction = model.predict(input_data)[0]
    return PredictResponse(predicted_price=prediction)