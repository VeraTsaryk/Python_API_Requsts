from pydantic import BaseModel, Field

class CommentModel(BaseModel):
    id: int = Field(gt=0)
    body: str = Field(min_length=1)
    postId: int = Field(gt=0)
