import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Use SQLite by default for easy local setup, or overwrite with DATABASE_URL
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///learning_path.db")

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
