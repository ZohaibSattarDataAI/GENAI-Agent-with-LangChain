from typing import TypedDict

class person(TypedDict):
    name: str
    age: int
    email: str

new_person: person = {
    "name": "John Doe",
    "age": 30,
    "email": "zabi86gmail.com" 
}

print(new_person)