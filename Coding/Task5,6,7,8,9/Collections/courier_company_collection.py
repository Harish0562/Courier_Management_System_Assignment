class CourierCompanyCollection:
    def __init__(self, company_name=None):
        self.company_name = company_name
        self.courier_details = []  # List of Courier objects
        self.employee_details = []  # List of Employee objects
        self.location_details = []  # List of Location objects

    def add_courier(self, courier_obj):
        self.courier_details.append(courier_obj)

    def add_employee(self, employee_obj):
        self.employee_details.append(employee_obj)

    def add_location(self, location_obj):
        self.location_details.append(location_obj)

    def __str__(self):
        return f"CourierCompanyCollection [Company Name={self.company_name}]"
