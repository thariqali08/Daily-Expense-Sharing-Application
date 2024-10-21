# Daily Expenses Sharing Application

## Project Overview
This project is a backend service for a daily-expenses sharing application. Users can add expenses and split them using three methods: equally, exact amounts, and percentages. The service manages users, expenses, and balance sheets, allowing users to view and download the balance sheets for tracking their expenses.

### Key Features
- **User Management**: Create, retrieve, and update user details.
- **Expense Management**: Add expenses, retrieve expenses for individual users, and manage different splitting methods.
- **Expense Splitting**:
  - **Equal**: Split the expenses equally among participants.
  - **Exact**: Specify the exact amount each participant owes.
  - **Percentage**: Split expenses based on percentages (ensures the total percentage adds up to 100%).
- **Balance Sheet**: View individual expenses and overall expenses for all users. Downloadable in CSV format.
- **API Endpoints**: Well-documented API with support for Postman or cURL testing.

## Setup Instructions

### Prerequisites
To run this project locally, you need to have the following installed:
- Python 3.x
- Django
- Django Rest Framework
- SQLite (for the database)

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/Daily-Expenses-Sharing-App.git
    cd Daily-Expenses-Sharing-App
    ```

2. **Set Up Virtual Environment**:
    - For Linux/Mac:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - For Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
3. **Apply Database Migrations**:
    ```bash
    python manage.py migrate
    ```
    
4. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
   The application will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

### User Endpoints
- **POST /api/users/**: Create a new user
  - Example:
    ```json
    {
      "email": "thariq@gmail.com",
      "name": "Thariq Ali",
      "mobile_number": "9791555000"
    }
    ```

- **GET /api/users/{id}/**: Retrieve user details
  - Example: `GET /api/users/1/`

### Expense Endpoints
- **POST /api/expenses/**: Add a new expense
  - Example:
    ```json
    {
      "description": "Lunch",
      "amount": 3000,
      "payer": 1,  # Payer's User ID
      "participants": [1, 2, 3],  # Participant IDs
      "split_method": "equal"  # Can be "equal", "exact", or "percentage"
    }
    ```

- **PATCH /api/expenses/{id}/**: Update an expense partially (e.g., only update the amount or description)
  - Example: `PATCH /api/expenses/1/`
    ```json
    {
      "amount": 3200
    }
    ```

- **DELETE /api/expenses/{id}/**: Delete an expense
  - Example: `DELETE /api/expenses/1/`

- **GET /api/expenses/{id}/balance-sheet/download/**: Download the balance sheet for a particular expense in CSV or PDF format.
  - Example: `GET /api/expenses/1/balance-sheet/download/`

## Using Postman for API Testing

### Step-by-Step Guide for Postman:

1. **Create a Collection**:
   - Open Postman and create a new collection to organize all your API requests.

2. **Create User Request**:
   - Create a `POST` request to `http://127.0.0.1:8000/api/users/`.
   - In the **Body** tab, choose `raw` and set the data type to `JSON`. Enter user data as shown:
     ```json
     {
      "email": "thariq@gmail.com",
      "name": "Thariq Ali",
      "mobile_number": "9791555000"
     }
     ```
   - Hit **Send** to create a new user.

3. **Add Expense Request**:
   - Create a `POST` request to `http://127.0.0.1:8000/api/expenses/`.
   - In the **Body** tab, enter the expense data:
     ```json
     {
       "description": "Stationery Things",
        "amount": "3500.00",
        "split_method": "percentage",
        "split_details": {
            "1": 50,
            "2": 25,
            "3": 25
        },
        "payer": 3,
        "participants": [1,2,3]
     },
     ```
   - Hit **Send** to add an expense.

4. **Retrieve Balance Sheet**:
   - Create a `GET` request to `http://127.0.0.1:8000/api/expenses/1/balance-sheet/download/`.
   - The balance sheet for the expense will be returned in your CSV format
