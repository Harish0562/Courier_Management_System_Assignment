class CourierCompany:
    def __init__(self, company_name=None, courier_details=None, employee_details=None, location_details=None):
        self.__company_name = company_name
        self.__courier_details = courier_details if courier_details is not None else []
        self.__employee_details = employee_details if employee_details is not None else []
        self.__location_details = location_details if location_details is not None else []

    def __str__(self):
        return f"CourierCompany [Name={self.__company_name}]"
