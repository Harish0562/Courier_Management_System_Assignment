def track_parcel_history(parcel_id, tracking_history):
    print(f"Tracking history for parcel {parcel_id}:")
    for update in tracking_history:
        print(update)

# Example usage
tracking_history = ["Location A", "Location B", "In Transit", "Delivered"]
track_parcel_history(1, tracking_history)
