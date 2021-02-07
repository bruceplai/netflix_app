from pydantic import BaseModel

class DataPoint(BaseModel):
  name: str
  value: int
