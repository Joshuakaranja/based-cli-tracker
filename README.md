# CLI-Based Skills Tracker

A command-line interface (CLI) application for tracking learning skills and practice sessions. This application allows users to manage their learning journey by adding skills, logging practice sessions, and monitoring progress.

## Features

- **User Management**: Add and manage users who are learning new skills
- **Skill Management**: Add skills for users and log practice sessions for each skill
- **Progress Tracking**: Track the time invested in practicing skills and monitor progress
- **Database Seeding**: Populate the database with sample data for testing and demonstration
- **Database Migrations**: Automated database schema management with Alembic

## Technologies Used

- Python 3.10 or higher
- SQLAlchemy for ORM
- Alembic for database migrations
- Click for CLI framework
- SQLite for data storage

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Joshuakaranja/based-cli-tracker.git
    cd based-cli-tracker
    ```

2. **Install dependencies using Pipenv:**

    ```bash
    pip install pipenv
    pipenv install
    ```

3. **Set up the database:**

    The application uses SQLite with the database file `skills_tracker.db`. No environment variables are needed as the database URL is configured in the application code.

    Run the migration to create database tables:

    ```bash
    pipenv run alembic upgrade head
    ```

4. **Optional: Seed the database with sample data:**

    ```bash
    pipenv run python main.py seed
    ```

## Usage

All commands should be run from the project root directory using pipenv:

### Available Commands

- **Seed Database**: Populate the database with sample data (users, skills, and practice sessions)

  ```bash
  pipenv run python main.py seed
  ```

- **Add User**: Add a new user

  ```bash
  pipenv run python main.py add-user "John Doe" "john.doe@example.com"
  ```

- **Add Skill**: Add a skill for a user (use the user ID)

  ```bash
  pipenv run python main.py add-skill 1 "Python Programming"
  ```

- **Log Practice**: Log practice time for a specific skill (use the user ID and skill name)

  ```bash
  pipenv run python main.py log-practice 1 "Python Programming" 60
  ```

### Example Workflow

1. **Set up the database:**
   ```bash
   pipenv run alembic upgrade head
   ```

2. **Add sample data:**
   ```bash
   pipenv run python main.py seed
   ```

3. **Add your own user:**
   ```bash
   pipenv run python main.py add-user "Your Name" "your.email@example.com"
   ```

4. **Add skills and start tracking:**
   ```bash
   pipenv run python main.py add-skill 4 "Web Development"
   pipenv run python main.py log-practice 4 "Web Development" 90
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Joshua Karanja  
Email: [jokaranja26@gmail.com](mailto:jokaranja26@gmail.com)  
GitHub: [Joshuakaranja](https://github.com/Joshuakaranja/based-cli-tracker)  

## Database Configuration

- **Database**: SQLite (`skills_tracker.db`)
- **Migrations**: Handled by Alembic
- **Git Ignore**: Database files are automatically ignored to prevent accidental commits

## Recent Updates

- ✅ Fixed database configuration to use unified `skills_tracker.db`
- ✅ Added database seeding functionality with sample data
- ✅ Updated CLI commands for better usability
- ✅ Added proper `.gitignore` configuration
- ✅ Verified application functionality with unified database

## Date

This README was last updated on September 2, 2024.