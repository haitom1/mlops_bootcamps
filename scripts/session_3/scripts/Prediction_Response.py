from pydantic import BaseModel

class PredictResponse(BaseModel):
    predicted_price: float