def format_address(street, city, state, zip_code):
    formatted_address = f"{street.title()}, {city.title()}, {state.upper()} {zip_code}"
    return formatted_address

# Example usage
print(format_address("123 main st", "springfield", "il", "62704"))
