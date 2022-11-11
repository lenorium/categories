from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

from config import Settings

settings = Settings(_env_file='.env')
connect_url = {
    'drivername': 'postgresql+psycopg2',
    'host': settings.db_host,
    'port': settings.db_port,
    'username': settings.db_user,
    'password': settings.db_password,
    'database': settings.db_name
}
engine = create_engine(URL(**connect_url), echo=True)
session_maker = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)
