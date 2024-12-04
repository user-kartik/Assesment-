# README 
# Registration API

This project is a Flask-based REST API for managing registration data, backed by a MySQL database. It includes CRUD operations for the `Registration` table.

## Prerequisites

1. **Python** (version 3.6 or higher)
2. **MySQL Server**
3. **pip** (Python package manager)
4. **Postman** or any other API testing tool (optional for testing)

## Installation Steps

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone <repository_url>
cd <repository_folder>
```

### Step 2: Set Up MySQL Database
1. Log in to your MySQL server:
   ```bash
   mysql -u root -p
   ```
2. Create a database:
   ```sql
   CREATE DATABASE yourdatabase;
   ```
3. Use the provided SQL script to create the `Registration` table:
   ```bash
   mysql -u root -p yourdatabase < create_registration_table.sql
   ```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install flask mysql-connector-python
```

### Step 4: Update Configuration
Edit the `app.py` file to replace the placeholders for database credentials:
- `yourpassword` with your MySQL password
- `yourdatabase` with your database name

### Step 5: Run the Flask Application
Start the Flask server:
```bash
python app.py
```

The application will be running at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. **Create Registration**
- **Endpoint**: `/register`
- **Method**: POST
- **Payload**:
  ```json
  {
      "Name": "John Doe",
      "Email": "john.doe@example.com",
      "DateOfBirth": "1990-01-01",
      "PhoneNumber": "1234567890",
      "Address": "123 Elm Street"
  }
  ```
- **Response**:
  ```json
  {
      "message": "Registration successful!",
      "ID": 1
  }
  ```

### 2. **Read All Registrations**
- **Endpoint**: `/registrations`
- **Method**: GET
- **Response**:
  ```json
  [
      {
          "ID": 1,
          "Name": "John Doe",
          "Email": "john.doe@example.com",
          "DateOfBirth": "1990-01-01",
          "PhoneNumber": "1234567890",
          "Address": "123 Elm Street",
          "RegistrationDate": "2024-12-04T08:00:00"
      }
  ]
  ```

### 3. **Update Registration**
- **Endpoint**: `/register/<id>`
- **Method**: PUT
- **Payload**:
  ```json
  {
      "Name": "John A. Doe",
      "Email": "john.adam.doe@example.com",
      "DateOfBirth": "1990-01-01",
      "PhoneNumber": "0987654321",
      "Address": "456 Oak Street"
  }
  ```
- **Response**:
  ```json
  {
      "message": "Registration updated successfully!"
  }
  ```

### 4. **Delete Registration**
- **Endpoint**: `/register/<id>`
- **Method**: DELETE
- **Response**:
  ```json
  {
      "message": "Registration deleted successfully!"
  }
  ```

## Testing the API
You can use **Postman** or **curl** to test the endpoints:

### Example curl commands:
- Create:
  ```bash
  curl -X POST http://127.0.0.1:5000/register \
       -H "Content-Type: application/json" \
       -d '{"Name": "John Doe", "Email": "john.doe@example.com", "DateOfBirth": "1990-01-01", "PhoneNumber": "1234567890", "Address": "123 Elm Street"}'
  ```
- Read:
  ```bash
  curl http://127.0.0.1:5000/registrations
  ```
- Update:
  ```bash
  curl -X PUT http://127.0.0.1:5000/register/1 \
       -H "Content-Type: application/json" \
       -d '{"Name": "John A. Doe", "Email": "john.adam.doe@example.com", "DateOfBirth": "1990-01-01", "PhoneNumber": "0987654321", "Address": "456 Oak Street"}'
  ```
- Delete:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/register/1
  ```

## License
This project is open-source and free to use.
