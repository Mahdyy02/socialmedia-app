from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# import psycopg2
# from psycopg2 import RealDictCursor
# import time

# while True:
#     try:
#         connection = psycopg2.connect(host= 'localhost', database= 'api_db',
#                                     user='postgres', password='mahdy', 
#                                     cursor_factory=RealDictCursor)
#         cursor = connection.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error: 
#         print("Connection to database failed")
#         print("Error: ", error)
#         time.sleep(2)

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionLocal = sessionmaker(autocommit = False,  autoflush= False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()