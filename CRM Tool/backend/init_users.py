import os

from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

import auth
from database import create_db_and_tables, engine
from models import User


def ensure_admin_user():
    print("Checking for existing users...")
    create_db_and_tables()
    
    admin_username = os.getenv("ADMIN_USERNAME", "admin")
    admin_password = os.getenv("ADMIN_PASSWORD", "admin123")
    
    with Session(engine) as session:
        existing_user = session.exec(select(User).where(User.username == admin_username)).first()
        if existing_user:
            print(f"User '{admin_username}' already exists.")
            return False

        print(f"Creating default user '{admin_username}'...")
        admin_user = User(
            username=admin_username,
            hashed_password=auth.get_password_hash(admin_password),
            is_active=True,
            is_admin=True
        )
        session.add(admin_user)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            existing_user = session.exec(select(User).where(User.username == admin_username)).first()
            if existing_user:
                print(f"User '{admin_username}' already exists.")
                return False
            raise
        print(f"Admin user '{admin_username}' created.")
        return True


def create_admin_user():
    return ensure_admin_user()

if __name__ == "__main__":
    ensure_admin_user()
