from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

# User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    skills = relationship("Skill", back_populates="user")

# Skill model
class Skill(Base):
    __tablename__ = 'skills'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="skills")
    practice_sessions = relationship("PracticeSession", back_populates="skill")

class PracticeSession(Base):
    __tablename__ = 'practice_sessions'
    
    id = Column(Integer, primary_key=True)
    duration = Column(Integer, nullable=False)  # Duration in minutes
    skill_id = Column(Integer, ForeignKey('skills.id'))
    
    skill = relationship("Skill", back_populates="practice_sessions")