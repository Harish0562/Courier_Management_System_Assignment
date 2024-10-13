def categorize_parcel(weight):
    if weight < 2.0:
        return "Light"
    elif 2.0 <= weight <= 5.0:
        return "Medium"
    else:
        return "Heavy"

# Example usage
weight = 3.5
print(categorize_parcel(weight))
