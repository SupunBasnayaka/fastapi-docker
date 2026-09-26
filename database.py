from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:supun@localhost:5430/fastapi_project"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

except Exception as e:
    print("Connection failed:")
    print(e)