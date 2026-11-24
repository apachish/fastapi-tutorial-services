from fastapi import FastAPI

app = FastAPI()

names_list = [
     {"id": 1, "age": 30, "name": "ghazal"},
     {"id": 2, "age": 32, "name": "maryam"},
     {"id": 3, "age": 40, "name": "mina"},
     {"id": 4, "age": 36, "name": "ali"},
     {"id": 5, "age": 25, "name": "ahmad"},
     {"id": 6, "age": 28, "name": "John"},
]

# list names
@app.get("/names")
async def retrives_name_list():
    return names_list

# create name
@app.post("/name")
async def create_name(name: dict):
    name_obj = {
        "id": len(names_list) + 1,
        "age": name["age"],
        "name": name["name"]
    }
    names_list.append(name_obj)
    return name_obj

# get details of a specific name
@app.get("/names/{name_id}")
async def retrives_name_details(name_id: int):
    for name in names_list:
        if name["id"] == name_id:
            return name
    return {"error": "Name not found"}

# retrieve the age of a specific name
@app.get("/names/{name_id}/age")
async def retrives_name_age(name_id: int):
    for name in names_list:
        if name["id"] == name_id:
            return {"age": name["age"]}
    return {"error": "Name not found"}

# update details of a specific name
@app.put("/names/{name_id}")
async def update_name_details(name_id: int, updated_name: dict):
    for i, name in enumerate(names_list):
        if name["id"] == name_id:
            names_list[i] = {**name, **updated_name}
            return names_list[i]
    return {"error": "Name not found"}

# delete details of a specific name
@app.delete("/names/{name_id}")
async def delete_name_details(name_id: int):
    for i, name in enumerate(names_list):
        if name["id"] == name_id:
            names_list.pop(i)
            return {"message": "Name deleted successfully"}
    return {"error": "Name not found"}

# default route
@app.get("/")
async def root():
    return {"message": "Hello World"}

