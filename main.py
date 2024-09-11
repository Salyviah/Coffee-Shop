from customer import Customer
from coffee import Coffee
from order import Order

def main():
    # Create some customers
    customer1 = Customer("Sally")
    customer2 = Customer("Brayo")

    # Create some coffees
    coffee1 = Coffee("Mocha")
    coffee2 = Coffee("ColdBrew")

    # Create some orders
    order1 = customer1.create_order(coffee1, 5.0)  # Sally orders Mocha
    order2 = customer1.create_order(coffee2, 6.0)  # Sally orders ClodBrew
    order3 = customer2.create_order(coffee1, 4.0)  # Brayo orders Mocha

    # Check customer orders
    print(f"{customer1.name} ordered: {[coffee.name for coffee in customer1.coffees()]}")
    print(f"{customer2.name} ordered: {[coffee.name for coffee in customer2.coffees()]}")

    # Check coffee orders
    print(f"{coffee1.name} has {coffee1.num_orders()} orders with an average price of {coffee1.average_price():.2f}")
    print(f"{coffee2.name} has {coffee2.num_orders()} orders with an average price of {coffee2.average_price():.2f}")

    
    most_spent_customer = Customer.most_aficionado(coffee1)
    if most_spent_customer:
        print(f"The customer who spent the most on {coffee1.name} is {most_spent_customer.name}")
    else:
        print(f"No customers have spent money on {coffee1.name} yet.")

if __name__ == "__main__":
    main()
