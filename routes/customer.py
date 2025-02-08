from bson import ObjectId
from fastapi import APIRouter, HTTPException
from pydantic import SecretStr
from starlette import status

from models.customer import Customer

from config.db import customer_collection

from schemas.customer import serializeDict, serializeList

customer = APIRouter()

@customer.get('/')
async def find_all_customers():
    customers = customer_collection.find()
    return serializeList(customers)


@customer.post('/')
async def create_customer(customer: Customer):
    customer_dict = dict(customer)
    if isinstance(customer_dict.get("password"), SecretStr):
        customer_dict["password"] = customer_dict["password"].get_secret_value()
    customer_collection.insert_one(customer_dict)
    return serializeDict(customer_dict)


@customer.put('/{id}')
async def update_customer(id: str, customer: Customer):
    customer_dict = customer.dict(exclude_unset=True)
    if 'password' in customer_dict:
        customer_dict['password'] = customer_dict['password'].get_secret_value()
    result = customer_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": customer_dict},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    return serializeDict(result)


@customer.delete('/{id}')
async def delete_customer(id: str):
    return serializeDict(customer_collection.find_one_and_delete({"_id": ObjectId(id)}))
