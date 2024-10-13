# services/courier_admin_service_impl.py
from connectionutil.db_connection import *

class CourierAdminServiceImpl:
    def __init__(self, company_obj):
        self.company_obj = company_obj

    def add_courier_staff(self, employee):
        # Establish a connection to the database
        connection = DBConnUtil.getConnection()
        try:
            cursor = connection.cursor()
            # Insert employee details into the Employee table
            insert_query = '''
            INSERT INTO Employee (employee_id, employee_name, email, contact_number, role, salary)
            VALUES (?, ?, ?, ?, ?, ?)
            '''
            cursor.execute(insert_query, 
                           (employee.get_employee_id(),  # Use provided employee ID
                            employee.get_employee_name(), 
                            employee.get_email(), 
                            employee.get_contact_number(), 
                            employee.get_role(), 
                            employee.get_salary()))
            connection.commit()
            print(f"Debug: Inserted employee ID: {employee.get_employee_id()}")  # Debug statement
            return employee.get_employee_id()
        except Exception as e:
            raise Exception(f"Error adding courier staff: {str(e)}")
        finally:
            cursor.close()
            connection.close()
