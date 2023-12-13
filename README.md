SAMPLE

# setting
+ pip3 install -r requirements.txt

+ select `Python: FastAPI` IN RUN AND DEBUG 
    + execute migration
    
+ If you change models.py
    + alembic revision --autogenerate -m "Description of the migration"
    + 再度`Python: FastAPI`を実行