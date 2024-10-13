def track_parcel(tracking_number, parcel_data):
    for parcel in parcel_data:
        if parcel[0] == tracking_number:
            print(f"Parcel {tracking_number} is {parcel[1]}")
            return
    print("Tracking number not found.")

# Example usage
parcel_data = [["TRACK001", "In Transit"], ["TRACK002", "Delivered"]]
track_parcel("TRACK001", parcel_data)
