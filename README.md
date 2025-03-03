**Password Generator (Django Project)**

This is a Django-based Password Generator that allows users to create strong and customizable passwords. 
Users can specify the password length and choose to include letters, numbers, and special characters.

**Features**
Generate random passwords of custom length (4-32 characters).
Select password components (letters, numbers, special characters).
Default to letters if no options are selected.
Copy password functionality (UI feature).
Simple and clean UI.

**Hosted Version**

You can access the hosted version of this app here: https://password-generator-7jya.onrender.com

**Tech Stack**

Backend: Django (Python)    
Frontend: HTML, CSS

**Assumptions And Solution**

User Inputs:
The user will enter the password length (minimum 4, maximum 32).
Default selection includes only alphabets (Stage 1).
User can select additional options via checkboxes (Stage 2).

Character Sets:
Alphabets (A-Z, a-z) – Default selection.
Numbers (0-9). 
Special Characters (!@#$%^&*...).

Password Generation Logic:
The app will randomly pick characters based on selected checkboxes.
The length of the password will match the user’s input.

Password Display: 
The generated password is shown in a text box.

Copy to Clipboard: 
The user can click a button to copy the password.

Error Handling:
If the user enters a length less than 4 or greater than 32, an error message appears.
If no checkboxes are selected, it automatically includes letters.

Deployment & Hosting:
The app is deployed for free on platform Render.


**Installation & Setup**

*  Clone the Repository:
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME

*  Create a Virtual Environment:
python -m venv venv

*  Install Dependencies:
pip install -r requirements.txt

*  Run Database Migrations:
python manage.py migrate

*  Run the Django Server:
python manage.py runserver

Now, open your browser and visit:
http://127.0.0.1:8000/

