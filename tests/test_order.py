import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initialization():
    coffee = Coffee("Latte")
    customer = Customer("Dan")
    order = Order(customer, coffee, 5.0)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_customer_validation():
    coffee = Coffee("Latte")
    with pytest.raises(ValueError):
        Order("NotACustomer", coffee, 5.0)  # Should raise an error

def test_order_coffee_validation():
    customer = Customer("Eve")
    with pytest.raises(ValueError):
        Order(customer, "NotACoffee", 5.0)  # Should raise an error

def test_order_price_validation():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)  # Price out of bounds

   
