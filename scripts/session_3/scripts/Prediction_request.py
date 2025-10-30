from pydantic import BaseModel

class PredictRequest(BaseModel):
    Avg_Area_Income: float
    Avg_Area_House_Age: float
    Avg_Area_Number_of_Rooms: float
    Avg_Area_Number_of_Bedrooms: float
    Area_Population: float