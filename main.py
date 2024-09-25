from fastapi import FastAPI

from tracking_system.routers import orders, samples

app = FastAPI()
app.include_router(orders.router)
app.include_router(samples.router)


@app.get('/')
def root():
    return {'message': 'Hello, world!'}
