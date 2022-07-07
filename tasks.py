from celery import Celery

app = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/1",
    backend="redis://127.0.0.1:6379/2"
)

@app.task
def multip(x, y):
    import time
    time.sleep(3)
    return x * y

@app.task
def divide(x, y):
    import time
    time.sleep(3)
    return x / y