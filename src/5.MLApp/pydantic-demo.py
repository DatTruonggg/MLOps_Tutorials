from pydantic import BaseModel

data = {
    "name" : "MDat",
    "age": "28", 
    "course": "MLOps",
    "rating": [4,4,'4','5', 4]
}

class Instructor(BaseModel):
    name: str
    age: int
    course: str 
    rating: list[int]  = []

user = Instructor(**data)

print(f"Found a instructor: {user}")