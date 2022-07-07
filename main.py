from fastapi import FastAPI
import tasks

app = FastAPI()


@app.get('/')
async def root():
    result = tasks.multip.delay(2, 2)
    return {"2*2": result.get()}