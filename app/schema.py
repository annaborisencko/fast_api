from typing import Literal
import datetime

from pydantic import BaseModel


class IdResponse(BaseModel):
    id: int


class SuccessResponse(BaseModel):
    status: Literal["success"]

class CreateUserRequest(BaseModel):
    name: str
    password: str

class CreateUserResponse(IdResponse):
    pass

class CreateAdvRequest(BaseModel):
    title: str
    description: str
    price: float
    user_id: int


class CreateAdvResponse(IdResponse):
    pass


class UpdateAdvRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None


class UpdateAdvResponse(SuccessResponse):
    pass


class GetAdvResponse(BaseModel):
    id: int  
    title: str
    description: str
    price: float
    user_id: int
    created_at: datetime.datetime



class SearchAdvResponse(BaseModel):
    results: list[GetAdvResponse]

class DeleteAdvResponse(SuccessResponse):
    pass
