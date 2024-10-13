def check_delivery_status(status):
    if status == "Delivered":
        return "The order has been delivered."
    elif status == "Processing":
        return "The order is still being processed."
    elif status == "Cancelled":
        return "The order has been cancelled."
    else:
        return "Unknown status."

# Example usage
status = "Delivered"
print(check_delivery_status(status))
