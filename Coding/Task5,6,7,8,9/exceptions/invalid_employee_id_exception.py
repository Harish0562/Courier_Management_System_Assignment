class InvalidEmployeeIdException(Exception):
    def __init__(self, employee_id):
        super().__init__(f"Employee ID {employee_id} is invalid.")
