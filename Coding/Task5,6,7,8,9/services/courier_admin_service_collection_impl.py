from services.courier_user_service_collection_impl import CourierUserServiceCollectionImpl
from services.icourier_admin_service import ICourierAdminService
from exceptions.invalid_employee_id_exception import InvalidEmployeeIdException
from collections.courier_company_collection import CourierCompanyCollection
from entities.employee import Employee

class CourierAdminServiceCollectionImpl(CourierUserServiceCollectionImpl, ICourierAdminService):
    def __init__(self, company_obj: CourierCompanyCollection):
        super().__init__(company_obj)

    def add_courier_staff(self, employee_obj: Employee):
        """Add a new courier staff member to the system"""
        if employee_obj is None or employee_obj.get_employee_id() is None:
            raise InvalidEmployeeIdException(employee_obj.get_employee_id())
        self.company_obj.add_employee(employee_obj)
        return employee_obj.get_employee_id()
