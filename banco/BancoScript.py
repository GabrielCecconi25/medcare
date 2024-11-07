from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class BancoScript:
    def connection():
        engine = create_engine('sqlite:///medcare.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def Select:
        session = connection()