from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# database connection (sqlite for simplicity)
engine = create_engine("sqlite:///project.db")

# Base class for models
Base = declarative_base()

# session factory
SessionLocal = sessionmaker(bind=engine)



