import pymysql
import sqlalchemy
from datetime import date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

mysql_info = {
    'user': 'root',
    'pass': '123123',
    'host': '127.0.0.1',
    'db_name': 'test',
}

engine = create_engine("mysql+pymysql://root:123123@127.0.0.1/test")
conn = engine.connect()
factory = sessionmaker(bind=engine)
session = factory()

Base = declarative_base()
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

def list_db():
    print("#################")
    users = Users.metadata.tables["users"]
    for instance in session.execute(users.select()):
        print(instance)
        print("---------")

def update_first_element(name):
    updated_rec = session.query(Users).filter_by(id=1).first()
    updated_rec.first_name = name
    session.commit()


def delete_elements():
    list = session.query(Users).filter(Users.id > 2).all()
    for deleted_item in list:
        session.delete(deleted_item)
        session.commit()

def insert_element():
    new_rec = Users(first_name="joao", last_name="januario machado")
    session.add(new_rec)
    session.commit()

print("\n------insert new element-----")
list_db()
insert_element()
list_db()

print("\n------update first element with date-----")
update_first_element("jonathan")
list_db()
update_first_element("jonathan" + date.today().strftime('%Y-%m-%d %H:%M:%S'))
list_db()


print("\n------delete ids higher then 2-----")
list_db()
delete_elements()
list_db()