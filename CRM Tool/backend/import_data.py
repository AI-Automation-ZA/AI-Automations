from datetime import datetime
from pathlib import Path

import pandas as pd
from sqlmodel import Session, SQLModel, func, select

from database import engine
from models import Account, Product, SalesPipeline, SalesTeam

DATA_DIR = Path(__file__).resolve().parents[2] / "CRM Data"

def clean_date(date_str):
    if pd.isna(date_str) or date_str == "":
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except:
        return None

def import_accounts():
    print("Importing accounts...")
    df = pd.read_csv(DATA_DIR / "accounts.csv")
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
    df = pd.read_csv(DATA_DIR / "products.csv")
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
    df = pd.read_csv(DATA_DIR / "sales_teams.csv")
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
    df = pd.read_csv(DATA_DIR / "sales_pipeline.csv")
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


def import_all_data_if_empty():
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        has_accounts = session.exec(select(func.count(Account.account))).one() > 0
        has_products = session.exec(select(func.count(Product.product))).one() > 0
        has_sales_teams = session.exec(select(func.count(SalesTeam.sales_agent))).one() > 0
        has_pipeline = session.exec(select(func.count(SalesPipeline.opportunity_id))).one() > 0

    imported = []

    if not has_accounts:
        import_accounts()
        imported.append("accounts")
    else:
        print("Accounts already loaded. Skipping import.")

    if not has_products:
        import_products()
        imported.append("products")
    else:
        print("Products already loaded. Skipping import.")

    if not has_sales_teams:
        import_sales_teams()
        imported.append("sales_teams")
    else:
        print("Sales teams already loaded. Skipping import.")

    if not has_pipeline:
        import_pipeline()
        imported.append("sales_pipeline")
    else:
        print("Sales pipeline already loaded. Skipping import.")

    return imported

if __name__ == "__main__":
    import_all_data_if_empty()
    print("Data ingestion complete!")
