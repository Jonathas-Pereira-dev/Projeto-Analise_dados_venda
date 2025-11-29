from fastapi import APIRouter, Depends
from sqlmodel import Session
from models import Order
from database import get_session

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/")
def list_orders(session: Session = Depends(get_session)):
    return session.query(Order).all()
