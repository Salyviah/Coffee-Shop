class Customer:
    _all_customers = []

    def __init__(self, name):
        self.name = name
        Customer._all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        from order import Order  # Delayed import to avoid circular dependency
        return [order for order in Order._all_orders if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        from order import Order  # Delayed import to avoid circular dependency
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        aficionado = None
        max_spent = 0
        for customer in cls._all_customers:
            spent = sum([order.price for order in customer.orders() if order.coffee == coffee])
            if spent > max_spent:
                max_spent = spent
                aficionado = customer
        return aficionado
