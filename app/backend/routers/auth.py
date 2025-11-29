from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import User
from database import get_session
import jwt
import hashlib
import os

router = APIRouter(prefix="/auth", tags=["Auth"])
JWT_SECRET = os.getenv("JWT_SECRET", "troque_isso")

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

@router.post("/signup")
def signup(email: str, password: str, session: Session = Depends(get_session)):
    exists = session.exec(select(User).where(User.email == email)).first()
    if exists:
        raise HTTPException(400, "Email já cadastrado")

    hashed = hash_password(password)
    user = User(email=email, password=hashed)
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"user": user}

@router.post("/login")
def login(email: str, password: str, session: Session = Depends(get_session)):
    hashed = hash_password(password)
    user = session.exec(select(User).where(User.email == email)).first()

    if not user or user.password != hashed:
        raise HTTPException(401, "Credenciais inválidas")

    token = jwt.encode({"user_id": user.id}, JWT_SECRET, algorithm="HS256")
    return {"token": token, "user": user}
