# Task Manager

A robust and user-friendly task management application built with Django and deployed on Vercel. 🌟

## Features

- User authentication (login, logout, registration)
- Create, read, update, and delete tasks
- Mark tasks as complete or incomplete
- Categorize tasks
- Set due dates for tasks
- Responsive design for mobile and desktop

## 🚀 Demo

Check out the live demo: [Task Manager App](http://your-live-demo-url.com)

## 🛠️ Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/task-manager.git
    cd task-manager
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use env\Scripts\activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables. Create a `.env` file in the root directory and add:

    ```dotenv
    SECRET_KEY=your_secret_key
    DEBUG=True
    POSTGRES_URL=your_database_url
    ```

5. Run migrations:

    ```bash
    python manage.py migrate
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser and navigate to [http://localhost:8000](http://localhost:8000)

## 📊 Database Schema

The application uses a PostgreSQL database with the following main model:

```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True)
