from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    career_goal = Column(String(255), nullable=True)
    experience_level = Column(String(50), nullable=True)

    skills = relationship("UserSkill", back_populates="user", cascade="all, delete-orphan")
    roadmaps = relationship("Roadmap", back_populates="user", cascade="all, delete-orphan")

class UserSkill(Base):
    __tablename__ = 'user_skills'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    skill_name = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False) # 'current', 'missing', 'completed'

    user = relationship("User", back_populates="skills")

class Roadmap(Base):
    __tablename__ = 'roadmaps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    generated_content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="roadmaps")
