from fastapi import FastAPI
from sqlalchemy import select

from schema import (
    CreateUserRequest,
    CreateUserResponse,
    CreateAdvRequest,
    CreateAdvResponse,
    DeleteAdvResponse,
    GetAdvResponse,
    SearchAdvResponse,
    UpdateAdvRequest,
    UpdateAdvResponse
)
from lifespan import lifespan
from dependancy import SessionDependency
from constants import SUCCESS_RESPONSE
import models
import crud

import datetime

app = FastAPI(
    title='Adv API',
    lifespan=lifespan
)

@app.post('/api/v1/user', response_model=CreateUserResponse)
async def create_user(User: CreateUserRequest, session: SessionDependency):
    user_dict = User.model_dump(exclude_unset=True)
    user_orm_obj = models.User(**user_dict)
    await crud.add_item(session, user_orm_obj)
    return user_orm_obj.id_dict


@app.post('/api/v1/advertisement', response_model=CreateAdvResponse)
async def create_adv(Adv: CreateAdvRequest, session: SessionDependency):
    Adv_dict = Adv.model_dump(exclude_unset=True)
    Adv_orm_obj = models.Adv(**Adv_dict)
    await crud.add_item(session, Adv_orm_obj)
    return Adv_orm_obj.id_dict


@app.get('/api/v1/advertisement/{adv_id}', response_model=GetAdvResponse)
async def get_adv(adv_id: int, session: SessionDependency):
    adv_orm_obj = await crud.get_item_by_id(session, models.Adv, adv_id)
    return adv_orm_obj.dict


@app.get('/api/v1/advertisement', response_model=SearchAdvResponse)
async def search_adv(
    session: SessionDependency,
    id: int = None,
    title: str = None,
    description: str = None,
    price: float = None,
    user_id: int = None,
    created_at: datetime.datetime = None
    ):
    
    query = select(models.Adv)
    conditions = []
    
    if id is not None:
        conditions.append(models.Adv.id == id)
    
    if title is not None:
        conditions.append(models.Adv.title.contains(title))
    
    if description is not None:
        conditions.append(models.Adv.description.contains(description))
    
    if price is not None:
        conditions.append(models.Adv.price == price)
    
    if user_id is not None:
        conditions.append(models.Adv.user_id == user_id)
    
    if created_at is not None:
        conditions.append(models.Adv.created_at == created_at)

    if conditions:
        query = query.where(*conditions)

    query = query.limit(10000)
    advs = await session.scalars(query)
    return {"results": [adv.dict for adv in advs]}


@app.patch('/api/v1/advertisement/{adv_id}', response_model=UpdateAdvResponse)
async def update_adv(adv_id: int, adv_data: UpdateAdvRequest, session: SessionDependency):
    adv_dict = adv_data.model_dump(exclude_unset=True)
    adv_orm_obj = await crud.get_item_by_id(session, models.Adv, adv_id)

    for field, value in adv_dict.items():
        setattr(adv_orm_obj, field, value)
    await session.commit()
    return SUCCESS_RESPONSE


@app.delete('/api/v1/advertisement/{adv_id}', response_model=DeleteAdvResponse)
async def delete_adv(adv_id: int, session: SessionDependency):
    adv_orm_obj = await crud.get_item_by_id(session, models.Adv, adv_id)
    await crud.delete_item(session, adv_orm_obj)
    return SUCCESS_RESPONSE
