from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ...config.ConfigData import setting

SQL_URI_CONNECTION = f"postgresql://{setting.database_user}:{setting.database_password}@{setting.database_host}:{setting.database_port}/{setting.database_name}"

engine = create_engine(SQL_URI_CONNECTION)
sessionLocal = sessionmaker(bind=engine, autoflush=False)
base = declarative_base()

def get_db(): 
    db = sessionLocal()
    try: 
        yield db
    finally: 
        db.close()