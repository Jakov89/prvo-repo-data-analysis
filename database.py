from sqlalchemy import create_engine,Column,Integer,String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

#username:password@host:port/database
engine = create_engine("mssql+pymssql://dbadmin:Qwerty123@smx2024.database.windows.net:1433/dataAnalytics")
session = sessionmaker(bind=engine)
sesija = session()
base = declarative_base()

class User(base):
    __tablename__ = "users_jakov"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)

class Employee(base):
    __tablename__ ="employees_jakov"

    id = Column(Integer,primary_key=True)
    full_name = Column(String)
    email = Column(String)
    age = Column(Integer)
    position = Column(String)
    salary = Column(Integer)
    years_in_company = Column(Integer)

class Product(base):
    __tablename__ = "products_jakov"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    price = Column(String)

class Sale(base):
    __tablename__ = "sales_jakov"

    id = Column(Integer,primary_key=True)

    employee_id = Column(ForeignKey("employees_jakov.id"))
    product_id = Column(ForeignKey("products_jakov.id"))

    product = relationship("Product")
    employee = relationship("Employee")




base.metadata.create_all(engine)

