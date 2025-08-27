# based-cli-tracker
# CLI Learning Tracker

A command-line interface (CLI) application for tracking learning skills and practice sessions. This application allows users to manage their learning journey by adding skills, logging practice sessions, and viewing their progress.

## Features

- **User Management**: Add and manage users who are learning new skills.
- **Skill Management**: Add skills for users and log practice sessions for each skill.
- **Progress Tracking**: Track the time invested in practicing skills and monitor progress.

## Technologies Used

- Python 3.10 or higher
- SQLAlchemy for ORM
- SQLite for data storage

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Joshuakaranja/based-cli-tracker.git
   cd based-cli-tracker
   ```

2. Install dependencies using Pipenv:

   ```bash
   pip install pipenv
   pipenv install
   ```

3. Create the database and tables:

   - Set Environment Variable:
   
     ```bash
     export DATABASE_URL="sqlite:///tracker.db"  # Example for Unix
     ```

   - Run the migration to create tables:

     ```bash
     pipenv run alembic upgrade head
     ```

## Usage

Run the CLI application using the following command:

```bash
PYTHONPATH=. python main.py
```

### Available Commands

- **Add User**: Add a new user.
  
  ```bash
  PYTHONPATH=. python main.py add-user "John Doe" "john.doe@example.com"
  ```

- **Add Skill**: Add a skill for a user (use the user ID).
  
  ```bash
  PYTHONPATH=. python main.py add-skill <user_id> "Skill Name"
  ```

- **Log Practice**: Log practice time for a specific skill (use the user ID and skill name).
  
  ```bash
  PYTHONPATH=. python main.py log-practice <user_id> "<skill_name>" <duration>
  ```

- **List Users**: List all users.
  
  ```bash
  PYTHONPATH=. python main.py list-users
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Joshua Karanja  
Email: [jokaranja26@gmail.com](mailto:jokaranja26@gmail.com)  
GitHub: [Joshuakaranja](https://github.com/Joshuakaranja/based-cli-tracker)  

## Date

This README was last updated on October 13, 2023.