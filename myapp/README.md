# E-commerce Lite

A robust FastAPI application with a PostgreSQL backend, designed for reliability and data persistence.

## Features
- **FastAPI**: Modern, high-performance web framework.
- **SQLAlchemy 2.0**: Powerful database toolkit and ORM.
- **Alembic**: Database migrations for schema management.
- **Docker Ready**: Fully containerized with Docker and Docker Compose.
- **Persistent Storage**: Configured with Docker Volumes to ensure your database data survives restarts and container removals.

---

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop/) and [Docker Compose](https://docs.docker.com/compose/install/)
- (Optional) Python 3.11+ for local development

### Running with Docker (Recommended)

1. **Build and Start**:
   ```bash
   docker-compose up --build
   ```
   This will start both the database and the web application.

2. **Run Migrations**:
   The first time you start the app, or after schema changes, run:
   ```bash
   docker-compose exec app alembic upgrade head
   ```

3. **Access the App**:
   - Application: [http://localhost:8000](http://localhost:8000)
   - API Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Health Check: [http://localhost:8000/health](http://localhost:8000/health)

---

### Running Locally

1. **Set up Environment**:
   Make sure you have a `.env` file with the correct `DATABASE_URL`.
   ```env
   DATABASE_URL=postgresql://postgres:1@localhost:5432/ecommerce
   SECRET_KEY=your_secret_key
   SESSION_SECRET=your_session_secret
   DEBUG=True
   ```

2. **Install Dependencies**:
   ```bash
   poetry install
   # OR
   pip install -r requirements.txt (if exported)
   ```

3. **Run Migrations**:
   ```bash
   alembic upgrade head
   ```

4. **Start the Server**:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Persistence Note
The database data is stored in a named Docker volume called `postgres_data`. This ensures that even if you stop and remove your containers (`docker-compose down`), your data will still be there the next time you run `docker-compose up`.
