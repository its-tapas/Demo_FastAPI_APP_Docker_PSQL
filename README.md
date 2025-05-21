# FastAPI Demo App deployed on Docker

This repository contains a FastAPI app that connects to a PostgreSQL database using Docker. The app is set up to run using Docker Compose.

---

## Prerequisites

1. **PostgreSQL Database**:
   - Create a database named `employeedb` using pgAdmin or SQL.
   - Inside `employeedb`, create a table called `employees` with the following columns:
![Table](https://github.com/user-attachments/assets/f96a6f2a-f48e-482d-b003-cf2a0a06bde9)


2. **Docker Desktop**:
   - Ensure Docker Desktop is installed on your machine.

---

## Setup and Run

### 1. Clone the Repository

```bash
git clone https://github.com/its-tapas/Demo_FastAPI_APP_Docker_PSQL.git
cd Demo_FastAPI_APP_Docker_PSQL
````

### 2. Create `.env` File

Create a file named `.env` in the root directory with the following content (replace values as needed):

```env
DATABASE_URL=postgresql://your_db_user:your_db_password@host.docker.internal:5432/employeedb
```
Replace user and password.

> ⚠️ Do not push this `.env` file to GitHub.

---

### 3. Run the Application

In the terminal, run:

```bash
docker-compose up --build
```

* This will start the FastAPI app in a Docker container.
* No need to add a new server in pgAdmin — it will use the existing local PostgreSQL database at port `5432`.
* The database data will persist even if Docker containers are shut down.

---

## Accessing the API

Once the containers are running:

* Open browser: [http://localhost:8000/docs](http://localhost:8000/docs)
* You can use the Swagger UI to test the API endpoints.

![Demo](https://github.com/user-attachments/assets/056b9851-0957-4b04-bd4f-bbc1d2fa156d)

---

## API Endpoints Overview

* **POST** `/employees/` – Create an employee
* **GET** `/employees/` – Get all employees
* **GET** `/employees/{employee_id}` – Get employee by ID
* **PUT** `/employees/{employee_id}` – Update employee
* **PATCH** `/employees/{employee_id}` – Partial update
* **DELETE** `/employees/{employee_id}` – Delete employee

---

## Example Request (POST /employees/)

```json
{
  "employee_name": "Alice Smith",
  "role": "Manager",
  "department": "HR"
}
```

---

## Notes

* Ensure `employeedb` and the `employees` table are created in pgAdmin before running the app.
* The FastAPI app connects to your existing local PostgreSQL instance, not a containerized one.
* You only need to update `DATABASE_URL` in the `.env` file with your actual PostgreSQL credentials.

---

## Security Best Practices

- **Environment Variables**:
  - Keep your database credentials (`your_db_user`, `your_db_password`) secure and never hardcode them in your application.
  - Use the `.env` file locally and configure secrets securely in production environments (e.g., using Docker secrets or CI/CD environment settings).

- **.gitignore**:
  - Ensure your `.env` file is listed in `.gitignore` to prevent accidental commits of sensitive information.

Example `.gitignore` snippet:
```
.env
**pycache**/
\*.py\[cod]
\*.log
venv/
```

## Optional Enhancements

- **Use `python-dotenv`** if you want to run the app locally outside Docker and load environment variables from `.env` in Python.
- **Unit tests** can be added using `pytest` and tested inside or outside Docker.
- **CI/CD integration** can be set up using GitHub Actions, GitLab CI, or other platforms.

## Contact

For issues, suggestions, or contributions, please open an issue or submit a pull request in the repository.



