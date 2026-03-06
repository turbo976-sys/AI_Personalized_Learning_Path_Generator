from sqlalchemy.orm import Session
from database import models
from datetime import datetime

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, username: str, career_goal: str = None, experience_level: str = None):
    db_user = models.User(username=username, career_goal=career_goal, experience_level=experience_level)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_skills(db: Session, user_id: int, skills_data: list):
    # skills_data is a list of dicts: [{'skill_name': 'Python', 'status': 'current'}, ...]
    # Clear old skills
    db.query(models.UserSkill).filter(models.UserSkill.user_id == user_id).delete()
    
    for sd in skills_data:
        db_skill = models.UserSkill(user_id=user_id, skill_name=sd['skill_name'], status=sd['status'])
        db.add(db_skill)
    db.commit()

def get_user_skills(db: Session, user_id: int):
    return db.query(models.UserSkill).filter(models.UserSkill.user_id == user_id).all()

def save_roadmap(db: Session, user_id: int, generated_content: str):
    db_roadmap = models.Roadmap(user_id=user_id, generated_content=generated_content, created_at=datetime.utcnow())
    db.add(db_roadmap)
    db.commit()
    return db_roadmap
