def track_courier(courier_id, locations):
    index = 0
    while index < len(locations):
        print(f"Tracking courier {courier_id}: {locations[index]}")
        index += 1
        if index == len(locations):
            print(f"Courier {courier_id} has reached the destination.")

# Example usage
locations = ["Location A", "Location B", "Location C"]
track_courier(1, locations)
