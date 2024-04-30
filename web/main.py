from fastapi import FastAPI

#object FastApi
app = FastAPI()

#var list
data = []

#membuat alamat utk halaman utama
#endpoint
@app.get("/")
def getHome():
    return{
        "messege": "ini halaman utama/home"
    }

@app.post("new")
def newData(add_data:dict):
    id = len(data) + 1
    add_data["id"] = id
   

    #memasukkan dict ke dalam list
    data.append(add_data)

    #return data yang ditambahkan
    return add_data
