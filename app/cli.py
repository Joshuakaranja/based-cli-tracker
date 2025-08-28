# app/cli.py
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User, Skill, PracticeSession

DATABASE_URL = "sqlite:///tracker.db"  

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

if __name__ == '__main__':
    cli()