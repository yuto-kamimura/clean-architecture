# setting
+ install essensial packages.
    + pip3 install -r requirements.txt

+ create tables in postgres.
    + select `Python: FastAPI` from RUN AND DEBUG
    + type url "http://127.0.0.1:8000/docs" and try post request.
    
+ if you changed models.py, please input command. you can adapt to tables in db.
    + `alembic revision --autogenerate -m "Description of the migration"`
    + execute debug with `Python: FastAPI` again or input command `alembic upgrade head`.