from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import date

class Account(SQLModel, table=True):
    account: str = Field(primary_key=True)
    sector: Optional[str] = None
    year_established: Optional[int] = None
    revenue: Optional[float] = None
    employees: Optional[int] = None
    office_location: Optional[str] = None
    subsidiary_of: Optional[str] = None

class Product(SQLModel, table=True):
    product: str = Field(primary_key=True)
    series: Optional[str] = None
    sales_price: Optional[float] = None

class SalesTeam(SQLModel, table=True):
    sales_agent: str = Field(primary_key=True)
    manager: Optional[str] = None
    regional_office: Optional[str] = None

class SalesPipeline(SQLModel, table=True):
    opportunity_id: str = Field(primary_key=True)
    sales_agent: Optional[str] = Field(default=None, foreign_key="salesteam.sales_agent")
    product: Optional[str] = Field(default=None, foreign_key="product.product")
    account: Optional[str] = Field(default=None, foreign_key="account.account")
    deal_stage: str
    engage_date: Optional[date] = None
    close_date: Optional[date] = None
    close_value: Optional[float] = None
