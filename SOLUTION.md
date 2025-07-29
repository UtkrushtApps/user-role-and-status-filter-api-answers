# Solution Steps

1. 1. Create a new FastAPI application structure with directories: app/ containing main.py, models.py, schemas.py, and database.py.

2. 2. In app/models.py, define a User SQLAlchemy model with id (int, PK), username (str), role (str), and status (str).

3. 3. In app/database.py, configure asynchronous SQLAlchemy engine and async_sessionmaker using the 'DATABASE_URL' environment variable. Provide a dependency-injectable get_async_session function for FastAPI.

4. 4. In app/schemas.py, define a Pydantic model UserOut reflecting the User model for response serialization (id, username, role, status).

5. 5. In app/main.py, configure the FastAPI app and implement an endpoint '/users' that receives optional 'role' and 'status' query parameters.

6. 6. In the /users endpoint, construct a SQLAlchemy select(User) statement, and add .where() clauses for each filter only if its parameter is provided. Combine the filters using AND logic by chaining .where() calls.

7. 7. Fetch all results asynchronously and return them serialized as a list of UserOut objects.

8. 8. Write a requirements.txt with FastAPI, Uvicorn, SQLAlchemy[asyncio], pydantic, and asyncpg.

9. 9. Write a Dockerfile to containerize the app: install Python dependencies, copy project files, and start Uvicorn.

10. 10. Add a docker-compose.yml to run both the app and a PostgreSQL database, and persist data in a Docker volume.

11. 11. Ensure that when both role and status are given as query parameters, only users matching BOTH (AND logic) are returned. When only one is given, filter appropriately. When neither is given, return all users.

12. 12. (Optional) Create tables and seed sample data for manual testing.

