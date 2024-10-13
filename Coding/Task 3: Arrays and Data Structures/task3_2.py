def find_nearest_available_courier(couriers):
    for courier in couriers:
        if courier['available']:
            return courier['name']
    return "No available couriers."

# Example usage
couriers = [{'name': 'Alice', 'available': True}, {'name': 'Bob', 'available': False}]
print(find_nearest_available_courier(couriers))
