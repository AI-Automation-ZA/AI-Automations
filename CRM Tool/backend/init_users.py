from sqlmodel import Session, select
from models import User
from database import engine, create_db_and_tables
import auth

def create_admin_user():
    print("Checking for existing users...")
    create_db_and_tables()
    with Session(engine) as session:
        existing_user = session.exec(select(User).where(User.username == "admin")).first()
        if existing_user:
            print("Admin user already exists.")
            return

        print("Creating default admin user...")
        admin_user = User(
            username="admin",
            hashed_password=auth.get_password_hash("admin123"), # In real app, prompt or random
            is_active=True,
            is_admin=True
        )
        session.add(admin_user)
        session.commit()
        print("Admin user 'admin' created with password 'admin123'")

if __name__ == "__main__":
    create_admin_user()
