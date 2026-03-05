# Django Student CRUD Application

This project provides CRUD APIs for student data using Django REST Framework and Swagger UI.

## Student fields
- `name`
- `age`
- `place`
- `phone_number`
- `state`

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API and Swagger URLs
- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`
- Student API base URL: `http://127.0.0.1:8000/api/students/`

## CRUD endpoints
- `POST /api/students/create/` - create student
- `GET /api/students/read/` - read all students
- `GET /api/students/read/{id}/` - read one student
- `PUT /api/students/update/{id}/` - full update
- `PATCH /api/students/update/{id}/` - partial update
- `DELETE /api/students/delete/{id}/` - delete student

### Example request body
```json
{
  "name": "Rahul",
  "age": 21,
  "place": "Bengaluru",
  "phone_number": "9876543210",
  "state": "Karnataka"
}
```
