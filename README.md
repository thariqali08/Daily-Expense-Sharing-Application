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
- **Balance Sheet**: View individual expenses and overall expenses for all users. Downloadable in CSV or PDF format.
- **API Endpoints**: Well-documented API with support for Postman and cURL testing.

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

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the project root directory for sensitive information like database settings or secret keys. You can use SQLite for local development, so the `.env` file might be as simple as:
     ```
     SECRET_KEY=your-secret-key-here
     DEBUG=True
     ```

5. **Apply Database Migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser**:
    To manage users and expenses via the Django admin panel:
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Development Server**:
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
      "email": "user@example.com",
      "name": "John Doe",
      "mobile_number": "1234567890"
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
       "email": "user@example.com",
       "name": "John Doe",
       "mobile_number": "1234567890"
     }
     ```
   - Hit **Send** to create a new user.

3. **Add Expense Request**:
   - Create a `POST` request to `http://127.0.0.1:8000/api/expenses/`.
   - In the **Body** tab, enter the expense data:
     ```json
     {
       "description": "Dinner",
       "amount": 5000,
       "payer": 1,
       "participants": [1, 2],
       "split_method": "percentage",
       "split_details": [
         {"user": 1, "percentage": 50},
         {"user": 2, "percentage": 50}
       ]
     }
     ```
   - Hit **Send** to add an expense.

4. **Retrieve Balance Sheet**:
   - Create a `GET` request to `http://127.0.0.1:8000/api/expenses/1/balance-sheet/download/`.
   - The balance sheet for the expense will be returned in your desired format (e.g., CSV or PDF).

### Testing with cURL

For users who prefer using `cURL` in the command line, here are a few examples:

- **Create User**:
  ```bash
  curl -X POST http://127.0.0.1:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "name": "John Doe", "mobile_number": "1234567890"}'
