from pydantic import BaseModel

class Title(BaseModel):
  id: str
  type: str
  title: str
  director: str
  castList: str
  country: str
  dateAdded: str
  releaseYear: str
  rating: str
  duration: str
  genre: str
  description: str
  