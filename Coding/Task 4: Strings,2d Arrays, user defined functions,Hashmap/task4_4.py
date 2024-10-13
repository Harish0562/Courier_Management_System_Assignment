def generate_order_confirmation(customer_name, order_number, delivery_address, expected_date):
    return f"Order Confirmation\n\nCustomer: {customer_name}\nOrder Number: {order_number}\nDelivery Address: {delivery_address}\nExpected Delivery Date: {expected_date}"

# Example usage
print(generate_order_confirmation("Arjun", "ORD123", "123 Main St, Springfield, IL", "2023-09-10"))
