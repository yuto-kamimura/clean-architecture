import psycopg2

def test_postgresql_connection():
    db_config = {
        "host": "localhost",
        "database": "postgres",
        "user": "postgres",
        "password": "postgres",
    }

    try:
        connection = psycopg2.connect(**db_config)
        print("db connection sucseeded.")
        connection.close()
    except psycopg2.OperationalError as e:
        print(f"connection error!: {e}")

# execute
test_postgresql_connection()
