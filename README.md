# Backend Documentation

## Overview
This backend is built using **FastAPI**, a modern web framework for Python. It is integrated with **AWS** services to ensure scalability, reliability, and performance. Additionally, it uses **PostgreSQL** as the primary relational database for data storage.

---

## Features
- RESTful API endpoints using FastAPI.
- Integration with AWS services such as S3, DynamoDB, and Lambda.
- Asynchronous processing for better performance.
- JWT-based authentication for secure access.
- PostgreSQL for relational database management.

---

## Prerequisites
- Python 3.8 or higher
- AWS account with necessary permissions
- PostgreSQL database setup
- Installed dependencies from `requirements.txt`

---

## Configuration

1. Create a `.env` file in the root directory:
    ```env
    AWS_ACCESS_KEY_ID=your_aws_access_key
    AWS_SECRET_ACCESS_KEY=your_aws_secret_key
    AWS_REGION=your_aws_region
    S3_BUCKET_NAME=your_s3_bucket_name
    POSTGRES_USER=your_postgres_user
    POSTGRES_PASSWORD=your_postgres_password
    POSTGRES_DB=your_postgres_db
    POSTGRES_HOST=your_postgres_host
    POSTGRES_PORT=your_postgres_port
    ```
    
2. Update `config.py` with your AWS, PostgreSQL, and application-specific settings.

---

## PostgreSQL Integration

- Used for relational database management.
- Example usage in `services/db_service.py`:
    ```python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    DATABASE_URL = "postgresql://user:password@host:port/dbname"

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    ```
- Ensure the database is properly configured and accessible.

---

## Testing

Run tests using `pytest`:
```bash
pytest
```

Ensure the PostgreSQL test database is set up and configured in the test environment.

---

## Deployment

1. Use AWS Elastic Beanstalk, ECS, or Lambda for deployment.
2. Configure CI/CD pipelines for automated deployment.
3. Ensure the PostgreSQL database is deployed and accessible in the production environment.

---

## License
This project is licensed under the MIT License.

