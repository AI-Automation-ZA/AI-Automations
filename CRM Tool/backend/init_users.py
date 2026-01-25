from sqlmodel import Session, select
from models import User
from database import engine, create_db_and_tables
import auth
import os

def create_admin_user():
    print("Checking for existing users...")
    create_db_and_tables()
    
    admin_username = os.getenv("ADMIN_USERNAME", "admin")
    admin_password = os.getenv("ADMIN_PASSWORD", "admin123")
    
    with Session(engine) as session:
        existing_user = session.exec(select(User).where(User.username == admin_username)).first()
        if existing_user:
            print(f"User '{admin_username}' already exists.")
            return

        print(f"Creating default user '{admin_username}'...")
        admin_user = User(
            username=admin_username,
            hashed_password=auth.get_password_hash(admin_password),
            is_active=True,
            is_admin=True
        )
        session.add(admin_user)
        session.commit()
        print(f"Admin user '{admin_username}' created.")

if __name__ == "__main__":
    create_admin_user()
