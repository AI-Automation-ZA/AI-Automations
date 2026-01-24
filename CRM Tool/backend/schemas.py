from typing import Optional, List
from pydantic import BaseModel
from datetime import date

class AccountBase(BaseModel):
    account: str
    sector: Optional[str]
    revenue: Optional[float]
    employees: Optional[int]

class DashboardStats(BaseModel):
    total_accounts: int
    total_products: int
    total_revenue_won: float
    total_deals_engaging: int

class PipelineItem(BaseModel):
    opportunity_id: str
    sales_agent: Optional[str]
    product: Optional[str]
    account: Optional[str]
    deal_stage: str
    close_value: Optional[float]

class Token(BaseModel):
    access_token: str
    token_type: str

class UserOut(BaseModel):
    username: str
    is_active: bool
    is_admin: bool
