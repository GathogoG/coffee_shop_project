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
    git clone https://github.com/yourusername/coffee-shop.git
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
print(f"Coffee Name: {coffee.name}")
print(f"Customer Name: {customer.name}")
print(f"Order Price: {order.price}")

# Check orders
print(f"Total Orders for {coffee.name}: {coffee.num_orders()}")
print(f"Average Price: {coffee.average_price()}")
print(f"Customers: {coffee.customers()}")
print(f"Customer Coffees: {customer.coffees()}")
print(f"Most Aficionado: {Customer.most_aficionado(coffee)}")
