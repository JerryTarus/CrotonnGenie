#### ----------- JERRY TARUS PHASE 3 PROJECT ----------

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# We start with category class
class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

# Then Supplier, has 4 attributes
class Supplier(Base):
    __tablename__ = 'supplier'
    supplier_id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_person = Column(String)
    contact_email = Column(String)
    contact_phone = Column(String)

# Product class
class Product(Base):
    __tablename__ = 'product'
    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    quantity_in_stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('category.category_id'))
    category = relationship("Category", backref="products")



#### ----------- JERRY TARUS PHASE 3 PROJECT ----------