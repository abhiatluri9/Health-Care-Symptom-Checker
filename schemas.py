from pydantic import BaseModel
from typing import List

class SymptomInput(BaseModel):
    text: str

class SymptomOutput(BaseModel):
    conditions: List[str]
    recommendations: List[str]
    disclaimer: str
