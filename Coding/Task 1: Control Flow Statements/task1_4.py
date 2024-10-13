def assign_couriers(couriers, shipments):
    assigned = {}
    for shipment in shipments:
        # Basic logic to assign a courier (for example, first available)
        for courier in couriers:
            if courier['available']:
                assigned[shipment['id']] = courier['name']
                courier['available'] = False  # Mark courier as assigned
                break
    return assigned

# Example usage
couriers = [{'name': 'Alice', 'available': True}, {'name': 'Bob', 'available': True}]
shipments = [{'id': 1}, {'id': 2}, {'id': 3}]
print(assign_couriers(couriers, shipments))
