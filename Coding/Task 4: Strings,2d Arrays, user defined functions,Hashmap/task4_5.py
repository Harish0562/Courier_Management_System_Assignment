def calculate_shipping_cost(source, destination, weight):
    base_cost = 5.00
    distance_cost = 0.50 * weight  # Example cost per weight
    total_cost = base_cost + distance_cost
    return total_cost

# Example usage
print(calculate_shipping_cost("New York", "Los Angeles", 10))  # Example weight
