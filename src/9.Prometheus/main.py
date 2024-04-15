from fastapi import FastAPI
import os 
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn

app = FastAPI()
port = int(os.environ.get("POST", 8005))

@app.get("/")
async def root():
    return {"message":"Hello world from FastApi"}

@app.get("/demo")
def demo_func():
    return {"message": "This is output from demo function"}

@app.post("/post_demo")
def demo_post():
    return {"message":"This is output demo fucntion"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

Instrumentator().instrument(app).expose(app)