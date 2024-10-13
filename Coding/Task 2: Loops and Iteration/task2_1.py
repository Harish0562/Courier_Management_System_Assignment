def display_orders(customer_id, orders):
    print(f"Orders for customer {customer_id}:")
    for order in orders:
        if order['customer_id'] == customer_id:
            print(order)

# Example usage
orders = [{'id': 1, 'customer_id': 1}, {'id': 2, 'customer_id': 2}, {'id': 3, 'customer_id': 1}]
display_orders(1, orders)
