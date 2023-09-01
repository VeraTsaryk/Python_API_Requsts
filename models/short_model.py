from pydantic import BaseModel, Field


class ShortModel(BaseModel):
    id: int = Field(gt=0)
