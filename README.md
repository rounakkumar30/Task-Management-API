# Task Management API

This project is a **Task Management System** built using **FastAPI** with JWT authentication and Redis caching. It supports CRUD operations for tasks, including creation, updating, deletion, and retrieval. The API also implements a priority queue for scheduling tasks based on priority and timestamp.

## Features

- **User Authentication**: JWT-based authentication.
- **Task Management**: CRUD operations (Create, Read, Update, Delete) for tasks.
- **Task Fields**: Tasks include title, description, status (pending/completed), and priority (low/medium/high).
- **Pagination & Filtering**: Support for pagination in task retrieval and filtering tasks based on priority and status.
- **Caching**: Redis is used to cache task retrieval for better performance.
- **Priority Queue**: Tasks are managed based on priority and timestamp using a priority queue (Min-Heap).
- **Unit Tests**: Pytest-based tests for API endpoints.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python** (>= 3.8)
- **PostgreSQL** (Database)
- **Redis** (for caching)
- **pip** (for installing dependencies)

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/task-management-api.git
cd task-management-api
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Database Setup

1. Ensure **PostgreSQL** is running and a database is created for this project. Update the `DATABASE_URL` in the `database.py` file to match your local PostgreSQL configuration.

2. Run migrations to create the tables:
```bash
alembic upgrade head
```

---

## Running the API

### Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## API Endpoints

### **1. User Registration**  
**POST** `/register`  
Registers a new user with a username and password.

**Request Body**:
```json
{
  "username": "testuser",
  "password": "password123"
}
```

**Response**:
```json
{
  "id": 1,
  "username": "testuser"
}
```

---

### **2. User Login**  
**POST** `/login`  
Logs in an existing user and returns a JWT token.

**Request Body**:
```json
{
  "username": "testuser",
  "password": "password123"
}
```

**Response**:
```json
{
  "access_token": "your_jwt_token_here",
  "token_type": "bearer"
}
```

---

### **3. Create Task**  
**POST** `/tasks/`  
Creates a new task with title, description, and priority.

**Request Body**:
```json
{
  "title": "My First Task",
  "description": "This is a test task",
  "priority": "high"
}
```

**Response**:
```json
{
  "id": 1,
  "title": "My First Task",
  "description": "This is a test task",
  "priority": "high",
  "status": "pending",
  "created_at": "2025-03-19T12:00:00"
}
```

---

### **4. Get Tasks**  
**GET** `/tasks/`  
Retrieves tasks with pagination and filtering options (by status and priority).

**Query Parameters**:
```text
skip=0&limit=10&priority=high&status=pending
```

**Response**:
```json
[
  {
    "id": 1,
    "title": "My First Task",
    "description": "This is a test task",
    "priority": "high",
    "status": "pending",
    "created_at": "2025-03-19T12:00:00"
  }
]
```

---

### **5. Update Task**  
**PUT** `/tasks/{task_id}`  
Updates an existing task's details.

**Request Body**:
```json
{
  "title": "Updated Task",
  "description": "This task has been updated",
  "priority": "medium"
}
```

**Response**:
```json
{
  "id": 1,
  "title": "Updated Task",
  "description": "This task has been updated",
  "priority": "medium",
  "status": "pending",
  "created_at": "2025-03-19T12:00:00"
}
```

---

### **6. Delete Task**  
**DELETE** `/tasks/{task_id}`  
Deletes a specific task by ID.

**Response**:
```json
{
  "message": "Task deleted successfully"
}
```

---

## Caching with Redis

Redis is used to cache task retrieval. Tasks will be cached for 60 seconds, reducing the load on the database.

---

## Running Unit Tests

Unit tests are written using **pytest**.

1. To run the tests, first activate the virtual environment:
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Run the tests with pytest:
```bash
pytest
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **FastAPI**: Web framework used for building the API.
- **Redis**: Caching mechanism.
- **PostgreSQL**: Database for storing tasks.
- **Pytest**: For testing the API endpoints.
