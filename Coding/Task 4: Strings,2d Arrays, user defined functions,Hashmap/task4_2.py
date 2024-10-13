import re

def validate_customer_data(data_type, data):
    if data_type == "name":
        return bool(re.match("^[A-Z][a-zA-Z]*$", data))
    elif data_type == "address":
        return not bool(re.search(r'[^a-zA-Z0-9\s,]', data))
    elif data_type == "phone":
        return bool(re.match(r'^\d{3}-\d{3}-\d{4}$', data))
    return False

# Example usage
print(validate_customer_data("name", "Arjun"))        # True
print(validate_customer_data("address", "123 Main St")) # True
print(validate_customer_data("phone", "123-456-7890")) # True
