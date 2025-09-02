# app/cli.py
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User, Skill, PracticeSession

DATABASE_URL = "sqlite:///skills_tracker.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """A CLI for tracking learning skills."""
    pass

@cli.command()
@click.argument('name')
@click.argument('email')
def add_user(name, email):
    """Add a new user."""
    session = Session()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    click.echo(f'User {name} added successfully.')

@cli.command()
@click.argument('user_id')
@click.argument('skill_name')
def add_skill(user_id, skill_name):
    """Add a new skill for a user."""
    session = Session()
    skill = Skill(name=skill_name, user_id=user_id)
    session.add(skill)
    session.commit()
    click.echo(f'Skill {skill_name} added for user ID {user_id}.')

@cli.command()
@click.argument('user_id')
@click.argument('skill_name')
@click.argument('duration')
def log_practice(user_id, skill_name, duration):
    """Log a practice session."""
    session = Session()
    skill = session.query(Skill).filter_by(name=skill_name, user_id=user_id).first()
    if skill:
        practice_session = PracticeSession(duration=duration, skill_id=skill.id)
        session.add(practice_session)
        session.commit()
        click.echo(f'Logged {duration} minutes of practice for skill {skill_name}.')
    else:
        click.echo(f'Skill {skill_name} not found for user ID {user_id}.')

@cli.command()
def seed():
    """Seed the database with sample data."""
    session = Session()

    # Create sample users
    users_data = [
        {"name": "Alice Johnson", "email": "alice@example.com"},
        {"name": "Bob Smith", "email": "bob@example.com"},
        {"name": "Charlie Brown", "email": "charlie@example.com"}
    ]

    users = []
    for user_data in users_data:
        user = User(name=user_data["name"], email=user_data["email"])
        session.add(user)
        users.append(user)

    session.commit()  # Commit to get user IDs

    skills_data = [
        {"name": "Python Programming", "user": users[0]},
        {"name": "Web Development", "user": users[0]},
        {"name": "Data Analysis", "user": users[1]},
        {"name": "Machine Learning", "user": users[1]},
        {"name": "Graphic Design", "user": users[2]},
        {"name": "Photography", "user": users[2]}
    ]

    skills = []
    for skill_data in skills_data:
        skill = Skill(name=skill_data["name"], user_id=skill_data["user"].id)
        session.add(skill)
        skills.append(skill)

    session.commit()  

    
    practice_data = [
        {"skill": skills[0], "duration": 60},
        {"skill": skills[0], "duration": 45},
        {"skill": skills[1], "duration": 90},
        {"skill": skills[2], "duration": 30},
        {"skill": skills[3], "duration": 120},
        {"skill": skills[4], "duration": 75},
        {"skill": skills[5], "duration": 50}
    ]

    for practice in practice_data:
        practice_session = PracticeSession(duration=practice["duration"], skill_id=practice["skill"].id)
        session.add(practice_session)

    session.commit()
    click.echo("Database seeded with sample data successfully!")

if __name__ == '__main__':
    cli()