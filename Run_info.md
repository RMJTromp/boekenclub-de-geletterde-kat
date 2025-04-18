# Initial Setup for the Project (First Run)

## Prerequisites
- Python 3.x installed
- pip installed
- Git (Optional, for cloning)

## Setup Steps

### 1. Get the Code
Clone or download the project files and navigate to the root directory:
```bash
git clone <your-repository-url>
cd <your-project-directory-name>
```

### 2. Create and Activate a Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate it (choose based on your OS)
# Windows:
.\.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate
```
You should see `(.venv)` in your terminal prompt when activated.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize Tailwind
```bash
python manage.py tailwind install
```

### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```
Follow the prompts to set username and password.

### 7. Run the Development Servers
You need **two separate terminals**, both with the virtual environment activated:

**Terminal 1: Run Tailwind Watcher**
```bash
python manage.py tailwind start
```
Leave this terminal running.

**Terminal 2: Run Django Development Server**
```bash
python manage.py runserver
```
Leave this terminal running.

### 8. Access the Site
Open your browser to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (or the address shown by runserver)
