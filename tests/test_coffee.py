import pytest
from coffee import Coffee
from customer import Customer
from order import Order


def test_coffee_initialization():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("A")  # Name must be at least 3 characters long

def test_coffee_orders():
    coffee = Coffee("Espresso")
    assert coffee.orders() == []

def test_coffee_customers():
    coffee = Coffee("Cappuccino")
    customer1 = Customer("John")
    customer2 = Customer("Jane")
    Order(customer1, coffee, 5.0)
    Order(customer2, coffee, 6.0)
    
    customers = coffee.customers()
    assert len(customers) == 2
    assert customer1 in customers
    assert customer2 in customers

def test_coffee_num_orders():
    coffee = Coffee("Americano")
    assert coffee.num_orders() == 0
    Order(Customer("Alice"), coffee, 4.0)
    assert coffee.num_orders() == 1

def test_coffee_average_price():
    coffee = Coffee("Mocha")
    assert coffee.average_price() == 0  # No orders yet
    Order(Customer("Bob"), coffee, 5.0)
    Order(Customer("Carol"), coffee, 7.0)
    assert coffee.average_price() == 6.0
