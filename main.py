import click
from crotonn_genie.database import (
    add_product, update_product, delete_product, search_product, export_to_json, initialize_database
)

def display_menu():
    click.echo("-------- Welcome to Crotonn Genie 💥💥💥 -----------")
    click.echo("Please select an option from the menu below:")
    click.echo("1. Add a new product")
    click.echo("2. Update a product")
    click.echo("3. Delete a product")
    click.echo("4. Search for products")
    click.echo("5. Export product data to JSON")
    click.echo("6. Exit")

def add():
    """Adding new product"""
    name = click.prompt('Product Name', type=str)
    price = click.prompt('Product Price', type=float)
    quantity = click.prompt('Quantity in Stock', type=int)
    category = click.prompt('Category Name', type=str)
    supplier = click.prompt('Supplier Name', type=str)
    contact_email = click.prompt('Supplier Email', type=str)
    contact_phone = click.prompt('Supplier Phone', type=str)
    add_product(name, price, quantity, category, supplier, contact_email, contact_phone)
    click.echo("Product added successfully ✅✅✅")

def update():
    """Updating a product"""
    product_id = click.prompt('Product ID', type=int)
    name = click.prompt('Product Name', type=str)
    price = click.prompt('Product Price', type=float)
    quantity = click.prompt('Quantity in Stock', type=int)
    update_product(product_id, name=name, price=price, quantity_in_stock=quantity)
    click.echo("Product updated successfully ✅✅✅")

def delete():
    """Deleting a product"""
    product_id = click.prompt('Product ID', type=int)
    delete_product(product_id)
    click.echo("Product deleted successfully ❌❌❌")

def search():
    """Searching for products"""
    keyword = click.prompt('Search Keyword', type=str)
    search_product(keyword)

def export():
    """Exporting product data to JSON file"""
    export_to_json()

def init_db():
    """Initialize database with initial data"""
    initialize_database()

if __name__ == "__main__":
    display_menu()
    option = click.prompt("Enter your choice (1-6)", type=int)

    if option == 1:
        add()
    elif option == 2:
        update()
    elif option == 3:
        delete()
    elif option == 4:
        search()
    elif option == 5:
        export()
    elif option == 6:
        click.echo("Exiting...")
    else:
        click.echo("Invalid choice. Please enter a number between 1 and 6.")
