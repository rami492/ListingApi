# Listing API  

A RESTful backend API for managing user listings, built with Django REST Framework and Knox for authentication.  

## Features  
- **User Authentication**: Secure token-based auth (register/login/logout) via Knox.  
- **CRUD Operations**: Create, read, update, and delete listings.  
- **Filtering**: Filter listings by `owner` or `title`, and users by fields like `username` or `email`.  
- **Pagination**: Built-in pagination (10 items per page).  

## Endpoints  
| Endpoint                | Method | Description                          | Auth Required |  
|-------------------------|--------|--------------------------------------|---------------|  
| `/listings/`            | GET    | List all listings                    | No            |  
| `/listings/`            | POST   | Create a new listing                 | Yes           |  
| `/listings/{id}/`       | GET    | Retrieve a listing                   | No            |  
| `/listings/{id}/`       | PUT    | Update a listing (owner only)        | Yes           |  
| `/users/`               | GET    | List all users                       | No            |  
| `/users/{id}/`          | GET    | Retrieve user details                | No            |  
| `/register/`            | POST   | Register a new user                  | No            |  
| `/login/`               | POST   | Login (returns auth token)           | No            |  
| `/logout/`              | POST   | Invalidate current token             | Yes           |  
| `/logoutall/`           | POST   | Invalidate all user tokens           | Yes           |  

## Tech Stack  
- **Backend**: Django REST Framework  
- **Authentication**: Knox (Token-based)  
- **Database**: PostgreSQL (or SQLite in dev)  
- **Filtering**: `django-filter`  

## Setup  
1. Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
```
2. Configure PostgreSQL variables in .env or use SQLite
3. Run migrations:
```bash
python3 manage.py makemigrations api1
```
```bash
python3 manage.py migrate api1
```
```bash
python3 manage.py makemigrations
```
```bash
python3 maage.py migrate
```
4. Start the server:
```bash
python3 manage.py runserver
```
