from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from models import Product
from database import get_session

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def list_products(session: Session = Depends(get_session)):
    return session.exec(select(Product)).all()

@router.get("/{product_id}")
def get_product(product_id: int, session: Session = Depends(get_session)):
    return session.get(Product, product_id)
