from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select, func
from typing import List
from datetime import timedelta

from database import get_session, create_db_and_tables
from import_data import import_all_data_if_empty
from init_users import ensure_admin_user
from models import Account, Product, SalesPipeline, User
import schemas
import auth

app = FastAPI(title="CRM Tool API", version="0.1.0")

# Security by Design: CORS Configuration
origins = [
    "http://localhost:3000", # Next.js dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    ensure_admin_user()
    import_all_data_if_empty()

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.username == form_data.username)).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the CRM Tool API"}

@app.get("/users/me", response_model=schemas.UserOut)
async def read_users_me(current_user: User = Depends(auth.get_current_active_user)):
    return current_user

@app.get("/dashboard", response_model=schemas.DashboardStats)
def get_dashboard_stats(
    session: Session = Depends(get_session),
    current_user: User = Depends(auth.get_current_active_user)
):
    # Total accounts
    total_accounts = session.exec(select(func.count(Account.account))).one()
    
    # Total products
    total_products = session.exec(select(func.count(Product.product))).one()
    
    # Total revenue from Won deals
    total_revenue_won = session.exec(
        select(func.sum(SalesPipeline.close_value)).where(SalesPipeline.deal_stage == "Won")
    ).one() or 0.0
    
    # Count of Engaging deals
    total_deals_engaging = session.exec(
        select(func.count(SalesPipeline.opportunity_id)).where(SalesPipeline.deal_stage == "Engaging")
    ).one()

    return {
        "total_accounts": total_accounts,
        "total_products": total_products,
        "total_revenue_won": total_revenue_won,
        "total_deals_engaging": total_deals_engaging
    }

@app.get("/accounts", response_model=List[schemas.AccountBase])
def list_accounts(
    offset: int = 0, 
    limit: int = 20, 
    session: Session = Depends(get_session),
    current_user: User = Depends(auth.get_current_active_user)
):
    accounts = session.exec(select(Account).offset(offset).limit(limit)).all()
    return accounts

@app.get("/pipeline", response_model=List[schemas.PipelineItem])
def list_pipeline(
    offset: int = 0, 
    limit: int = 20, 
    session: Session = Depends(get_session),
    current_user: User = Depends(auth.get_current_active_user)
):
    items = session.exec(select(SalesPipeline).offset(offset).limit(limit)).all()
    return items
