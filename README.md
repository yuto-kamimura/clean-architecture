# setting
+ pip3 install -r requirements.txt

+ select `Python: FastAPI` IN RUN AND DEBUG 
    + create tables in postgres
    
+ If you change models.py
    + alembic revision --autogenerate -m "Description of the migration"
    + execute debug with `Python: FastAPI` again.