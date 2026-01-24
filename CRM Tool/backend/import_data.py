import pandas as pd
from sqlmodel import Session, SQLModel, create_engine, select
from models import Account, Product, SalesTeam, SalesPipeline
from database import engine
import os
from datetime import datetime

DATA_DIR = "../../CRM Data"

def clean_date(date_str):
    if pd.isna(date_str) or date_str == "":
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except:
        return None

def import_accounts():
    print("Importing accounts...")
    df = pd.read_csv(os.path.join(DATA_DIR, "accounts.csv"))
    with Session(engine) as session:
        for _, row in df.iterrows():
            account = Account(
                account=row["account"],
                sector=row["sector"],
                year_established=int(row["year_established"]) if not pd.isna(row["year_established"]) else None,
                revenue=float(row["revenue"]) if not pd.isna(row["revenue"]) else None,
                employees=int(row["employees"]) if not pd.isna(row["employees"]) else None,
                office_location=row["office_location"],
                subsidiary_of=row["subsidiary_of"] if not pd.isna(row["subsidiary_of"]) else None
            )
            session.merge(account)
        session.commit()

def import_products():
    print("Importing products...")
    df = pd.read_csv(os.path.join(DATA_DIR, "products.csv"))
    with Session(engine) as session:
        for _, row in df.iterrows():
            product = Product(
                product=row["product"],
                series=row["series"],
                sales_price=float(row["sales_price"]) if not pd.isna(row["sales_price"]) else None
            )
            session.merge(product)
        session.commit()

def import_sales_teams():
    print("Importing sales teams...")
    df = pd.read_csv(os.path.join(DATA_DIR, "sales_teams.csv"))
    with Session(engine) as session:
        for _, row in df.iterrows():
            team = SalesTeam(
                sales_agent=row["sales_agent"],
                manager=row["manager"],
                regional_office=row["regional_office"]
            )
            session.merge(team)
        session.commit()

def import_pipeline():
    print("Importing sales pipeline...")
    df = pd.read_csv(os.path.join(DATA_DIR, "sales_pipeline.csv"))
    with Session(engine) as session:
        for _, row in df.iterrows():
            pipeline = SalesPipeline(
                opportunity_id=row["opportunity_id"],
                sales_agent=row["sales_agent"],
                product=row["product"],
                account=row["account"] if not pd.isna(row["account"]) else None,
                deal_stage=row["deal_stage"],
                engage_date=clean_date(row["engage_date"]),
                close_date=clean_date(row["close_date"]),
                close_value=float(row["close_value"]) if not pd.isna(row["close_value"]) else None
            )
            session.merge(pipeline)
        session.commit()

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    import_accounts()
    import_products()
    import_sales_teams()
    import_pipeline()
    print("Data ingestion complete!")
