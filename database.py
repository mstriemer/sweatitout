import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dev_db = "sqlite:///sweatitout.db"
engine = create_engine(os.environ.get('DATABASE_URL', dev_db))

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models import Registration
    Base.metadata.create_all(bind=engine)
