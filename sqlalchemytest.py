import pymysql
import sqlalchemy
from datetime import date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

######### CONNECTING #########  
mysql_info = {
    'user': 'root',
    'pass': '123123',
    'host': '127.0.0.1',
    'db_name': 'test',
}
engine = create_engine("mysql+pymysql://root:123123@127.0.0.1/test")
conn = engine.connect()
######### CREATE SESSION ######### 
factory = sessionmaker(bind=engine)
session = factory()




######### MAPPING CLASS OF USER TABLE ######### 
Base = declarative_base()
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

######### BOOTSTRAPING TABLE #########
session.add(Users(first_name="will", last_name="smith"))
session.add(Users(first_name="carlton", last_name="banks"))
session.add(Users(first_name="hillary", last_name="banks"))
session.commit()



######### LISTING ALL INSIDE USERS TABLE ######### 
def list_db():
    print("#################")
    users = Users.metadata.tables["users"]
    for instance in session.execute(users.select()):
        print(instance)
        print("---------")

######### UPDATE FIRST ELEMENT NAME ######### 
def update_first_element(name):
    updated_rec = session.query(Users).first()
    updated_rec.first_name = name
    session.commit()

######### DELETING ELEMENTS WITH ID HIGHER THEN 2 ######### 
def delete_last_element():
    all_users = session.query(Users).all()
    list = session.query(Users).filter(Users.id == all_users[-1].id).all()
    for deleted_item in list:
        session.delete(deleted_item)
        session.commit()

######### CLEAN_TABLE ######### 
def delete_all_elements():
    list = session.query(Users).all()
    for deleted_item in list:
        session.delete(deleted_item)
        session.commit()

######### INSERTING ELEMENTS ######### 
def insert_element():
    new_rec = Users(first_name="uncle", last_name="phil")
    session.add(new_rec)
    session.commit()

print("\n------insert new element-----")
list_db()
insert_element()
list_db()

print("\n------update first element with date-----")
update_first_element("will")
list_db()
update_first_element("will" + date.today().strftime('%Y-%m-%d %H:%M:%S'))
list_db()


print("\n------delete ids higher then 2-----")
list_db()
delete_last_element()
list_db()

delete_all_elements()