

class Coffee:
    _all_coffees = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters")
        self._name = name
        Coffee._all_coffees.append(self)

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order  # Delayed import to avoid circular dependency
        return [order for order in Order._all_orders if order.coffee == self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        total_price = sum(order.price for order in self.orders())
        num_orders = len(self.orders())
        return total_price / num_orders if num_orders > 0 else 0
