import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def test_customer_initialization():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")  # Name must be between 1 and 15 characters

    with pytest.raises(ValueError):
        Customer("ThisNameIsWayTooLong")  # Exceeds 15 characters

def test_customer_orders():
    customer = Customer("Bob")
    assert customer.orders() == []

def test_customer_coffees():
    customer = Customer("Eve")
    coffee1 = Coffee("Flat White")
    coffee2 = Coffee("Cortado")
    Order(customer, coffee1, 4.5)
    Order(customer, coffee2, 5.0)

    coffees = customer.coffees()
    assert len(coffees) == 2
    assert coffee1 in coffees
    assert coffee2 in coffees

def test_customer_create_order():
    customer = Customer("Mallory")
    coffee = Coffee("Macchiato")
    order = customer.create_order(coffee, 5.5)
    assert order in customer.orders()

def test_customer_most_aficionado():
    coffee = Coffee("Espresso")
    customer1 = Customer("John")
    customer2 = Customer("Jane")
    Order(customer1, coffee, 5.0)
    Order(customer1, coffee, 5.0)
    Order(customer2, coffee, 6.0)
    
    assert Customer.most_aficionado(coffee) == customer1
