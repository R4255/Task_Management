Task Manager
A robust and user-friendly task management application built with Django and deployed on Vercel.
🌟 Features

User authentication (login, logout, registration)
Create, read, update, and delete tasks
Mark tasks as complete or incomplete
Categorize tasks
Set due dates for tasks
Responsive design for mobile and desktop

🚀 Demo
Check out the live demo: Task Manager App
🛠️ Installation

Clone the repository:
Copygit clone https://github.com/your-username/task-manager.git
cd task-manager

Create a virtual environment and activate it:
Copypython -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

Install the required packages:
Copypip install -r requirements.txt

Set up your environment variables. Create a .env file in the root directory and add:
CopySECRET_KEY=your_secret_key
DEBUG=True
POSTGRES_URL=your_database_url

Run migrations:
Copypython manage.py migrate

Start the development server:
Copypython manage.py runserver

Open your browser and navigate to http://localhost:8000

📊 Database Schema
The application uses a PostgreSQL database with the following main model:
pythonCopyclass Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True)
🚢 Deployment
This project is configured for deployment on Vercel. The vercel.json file in the root directory contains the necessary configuration.
To deploy:

Install the Vercel CLI: npm i -g vercel
Run vercel --prod in the project root
Follow the prompts to link your Vercel account and project
