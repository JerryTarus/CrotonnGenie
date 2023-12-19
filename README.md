# Crotonn Genie 💥💥💥


# Welcome to Crotonn Genie! This is a simple command-line interface (CLI) application for managing product data. With Crotonn Genie, you can perform various operations such as adding, updating, and deleting products, searching for products, and exporting product data to JSON.

### Table of Contents
### Getting Started
### Prerequisites
### Installation
### Usage
### Menu
### Adding a Product
### Updating a Product
### Deleting a Product
### Searching for Products
### Exporting Product Data to JSON
### Database
### Initialization
### Models
### Category
### Supplier
### Product
### Contributing
### License

This is how the app looks like:

![Alt text](<Screenshot from 2023-12-19 13-42-20.png>)

![Alt text](<Screenshot from 2023-12-19 13-41-18.png>)

# Getting Started
### Prerequisites
### Make sure you have Python installed.

# Installation

## Clone the repository:
### git clone git@github.com:JerryTarus/crotonngenie.git

## Install dependencies:
### pip install -r requirements.txt

## Or
### pipenv install sqlalchemy alembic click

# Usage
## Menu

## To start Crotonn Genie, run the following command:
### pipenv run python main.py menu


## Adding a Product
### To add a new product, select option 1 from the menu and follow the prompts.

## Updating a Product
### To update a product, select option 2 from the menu and follow the prompts.

## Deleting a Product
### To delete a product, select option 3 from the menu and follow the prompts.

## Searching for Products
### To search for products, select option 4 from the menu and enter the search keyword.

## Exporting Product Data to JSON
### To export product data to a JSON file, select option 5 from the menu.

## Database
## Initialization
### The database is initialized with initial data by running the init_db command.

### pipenv run python main.py init_db


## Models
## Category
### The Category class represents a product category.

## Supplier
### The Supplier class represents a product supplier.

## Product
### The Product class represents a product with details such as name, price, quantity in stock, and category.


## License
### This project is licensed under the MIT License - see the LICENSE file for details.
