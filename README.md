# Giaic_quearter_4_assignment_2

## Overview

This project is a **FastAPI-based backend application** simulating a simple bank transfer system. It demonstrates basic REST API creation, user authentication, and in-memory data manipulation without a database. The project is designed for educational purposes and showcases API endpoints, request/response handling, and testing via Swagger UI.

---

## Features

* **/authenticate Endpoint**: Authenticates a user based on `name` and `pin_number`. Returns user details including current `balance`.
* **/bank-transfer Endpoint**: Transfers a specified amount from a sender to a receiver. Deducts the amount from the sender and adds it to the receiver.
* **In-Memory Database**: Users are stored in a Python list, simulating a simple database.
* **Swagger UI Integration**: Easily test the endpoints via `/docs`.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/assignment_2.git
cd assignment_2
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Add dependencies:

```bash
uv add fastapi
pip install fastapi uvicorn
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Open your browser and navigate to:

```
http://127.0.0.1:8000/docs
```

This will open the Swagger UI for testing the API endpoints.

---

## API Endpoints

### 1. **Authenticate User**

* **Endpoint**: `/authenticate`
* **Method**: POST
* **Request Body**:

```json
{
  "name": "Ali",
  "pin_number": "1234"
}
```

* **Response**:

```json
{
  "message": "Authenticated Successfully",
  "user": {
    "name": "Ali",
    "pin": "1234",
    "balance": 1000
  }
}
```

### 2. **Bank Transfer**

* **Endpoint**: `/bank-transfer`
* **Method**: POST
* **Request Body**:

```json
{
  "sender_name": "Ali",
  "receiver_name": "Umar",
  "amount": 200
}
```

* **Response**:

```json
{
  "message": "Transfer Successful",
  "sender": {
    "name": "Ali",
    "pin": "1234",
    "balance": 800
  },
  "receiver": {
    "name": "Umar",
    "pin": "4321",
    "balance": 700
  }
}
```

### 3. **Re-Authenticate Receiver**

* **Endpoint**: `/authenticate`
* **Method**: POST
* **Request Body**:

```json
{
  "name": "Umar",
  "pin_number": "4321"
}
```

* **Response**:

```json
{
  "message": "Authenticated Successfully",
  "user": {
    "name": "Umar",
    "pin": "4321",
    "balance": 700
  }
}
```

---

## Testing

* Open `/docs` in your browser to access the Swagger UI.
* Use the **Try it out** buttons to test authentication and transfers.
* Responses will reflect updated balances after transfers.

---

## Project Structure

```
assignment_2/
│
├── main.py          # FastAPI application with all endpoints
├── README.md        # Project documentation
├── venv/            # Python virtual environment (optional)
```

---

## Notes

* This project uses an **in-memory user list**; all data resets on server restart.
* For production, replace the in-memory list with a proper database (e.g., SQLite, PostgreSQL).
* No frontend is required; testing is done via Swagger UI.

---

## Author

**Muhammad Umar**

* FastAPI Backend Assignment - Quarter 4
* GitHub: [[https://github.com/yourusername/assignment_2](](https://github.com/yourusername/assignment_2]%28)[https://github.com/yourusername/assi](https://github.com/yourusername/assi)
