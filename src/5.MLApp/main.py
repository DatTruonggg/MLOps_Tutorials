from fastapi import FastAPI

app = FastAPI()
@app.get('/')
async def root():
    return{"message": "Hello World from FASTAPI"}

@app.get('/demo')
def demo_func():
    return{"message": "Just demo function!!!!"}

@app.post('/post_demo')
def post():
    return{"message": "POST DEMO"}