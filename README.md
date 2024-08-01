# VRP_CRUD

This project is a web application built with Python and Django that allows users to order laptops. It includes CRUD (Create, Read, Update, Delete) operations for managing laptop orders.

## Technologies Used

- Python
- Django
- HTML
- CSS
- MySQL

## Features

- **User Authentication**: Users can register, login, and manage their accounts.
- **Order Management**: CRUD operations for creating, reading, updating, and deleting laptop orders.
- **Responsive Design**: HTML and CSS used for a responsive and user-friendly interface.
- **Database**: MySQL used to store and manage data efficiently.

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Chay-Dhanush/VRP_Crud/
   cd Crud

2. **Create virtual environment**
   First of all create enviroment in your local and then install these dependencies
   ```bash
   py -m venv environmentname
 
3. **Install dependencies**
   ```bash
   pip install python
   pip install django
   pip install mysqlclient
   
4. **Database Setup**

   1) Ensure MySQL is installed and running.
   2) Update DATABASES configuration in 'settings.py' with your MySQL credentials.

6. **Run Migrations**
   ```bash
   py manage.py makemigrations
   py manage.py migrate

7. **Runserver**
   ```bash
   py manage.py runserver
   

