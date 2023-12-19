#### ----------- JERRY TARUS PHASE 3 PROJECT ----------
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crotonn_genie.models import Base, Product, Category, Supplier

engine = create_engine('sqlite:///crotonn_genie.db')

# This is a session
Session = sessionmaker(bind=engine)
session = Session()


def initialize_database():
    """I initialised data here"""
    Base.metadata.create_all(engine)  
    if session.query(Product).count() > 0 or session.query(Category).count() > 0 or session.query(Supplier).count() > 0:
        print("Database already initialized with data.")
        return

    
def add_product(name, price, quantity, category_name, supplier_name, contact_email, contact_phone):
    # Here we query an existing category or create a new one
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()

    # Here we query an existing supplier or create a new one
    supplier = session.query(Supplier).filter_by(name=supplier_name).first()
    if not supplier:
        supplier = Supplier(name=supplier_name, contact_email=contact_email, contact_phone=contact_phone)
        session.add(supplier)
        session.commit()

    # Then we create a product using an existing category, notice when you run it
    new_product = Product(name=name, price=price, quantity_in_stock=quantity, category=category)
    session.add(new_product)
    session.commit()

# Update product  
def update_product(product_id, **kwargs):
    product = session.query(Product).filter_by(product_id=product_id).first()
    if product:
        for key, value in kwargs.items():
            setattr(product, key, value)
        session.commit()
    else:
        print("Oup! product not found ❗❗❗")
        
# Deleting a Product
def delete_product(product_id):
    product = session.query(Product).filter_by(product_id=product_id).first()
    if product:
        session.delete(product)
        session.commit()
        print("Product deleted successfully ✅✅✅")
    else:
        print("Product not found ❗❗❗")
        
# Seach for product        
def search_product(keyword):
    products = session.query(Product).filter(Product.name.ilike(f"%{keyword}%")).all()

    for product in products:
        print(f"Product ID: {product.product_id}, Name: {product.name}, "
              f"Price: {product.price}, Quantity in Stock: {product.quantity_in_stock}")
        
        if product.category:
            print(f"Category: {product.category.name}")
        
        # This line checks if product has supplier associated and prints supplier details if available
        if hasattr(product, 'supplier'):
            print(f"Supplier: {product.supplier.name}, Contact: {product.supplier.contact_email}, "
                  f"Phone: {product.supplier.contact_phone}")
        else:
            print("Supplier information not available for this product❗❗")

        print("")

    if not products:
        print("No matching products found ❗❗❗")

        
        
def export_to_json():
    products = session.query(Product).all()
    exported_data = []

    for product in products:
        product_data = {
            "Product ID": product.product_id,
            "Name": product.name,
            "Price": product.price,
            "Quantity in Stock": product.quantity_in_stock
        }

        if product.category:
            product_data["Category"] = product.category.name

        # Check if product has supplier associated and add supplier details if available
        if hasattr(product, 'supplier'):
            product_data["Supplier"] = {
                "Name": product.supplier.name,
                "Contact": product.supplier.contact_email,
                "Phone": product.supplier.contact_phone
            }

        exported_data.append(product_data)

    with open('product_data.json', 'w') as file:
        json.dump(exported_data, file, indent=4)

    print("Product data exported to product_data.json successfully ✅✅✅")