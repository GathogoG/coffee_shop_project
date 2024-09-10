class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee.")
            
        self._customer = customer
        self._coffee = coffee
        self._price = price

        coffee._orders.append(self)  # Add the order to the coffee's orders
        customer._orders.append(self)  # Add the order to the customer's orders

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
