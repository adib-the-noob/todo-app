from pydantic import BaseModel
from pydantic.fields import Field

class UserAuthSchema(BaseModel):
    name : str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    
    class Config:
        from_attributes = True

class UserInDB(UserAuthSchema):
    id: int = Field(...)
    
    class Config:
        from_attributes = True
    