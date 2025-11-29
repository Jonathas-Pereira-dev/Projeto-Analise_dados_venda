from fastapi import FastAPI
from routers import auth, products, orders

app = FastAPI(title="Loja de Terços - API")

app.include_router(auth.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"status": "OK"}
