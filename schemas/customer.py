from bson import ObjectId

from models.customer import Customer


def serializeDict(customer: dict) -> dict:
    if "_id" in customer and isinstance(customer["_id"], ObjectId):
        customer["_id"] = str(customer["_id"])
    return {key: value for key, value in customer.items() if key != "password"} # Excluding the password field from the output


def serializeList(customers: list) -> list:
    return [serializeDict(customer) for customer in customers]