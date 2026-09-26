from database import engine
from sqlalchemy import text

with engine.connect() as connection:

    result = connection.execute(
        text("SELECT name FROM users")
    )

    for row in result:
        print(row[0])