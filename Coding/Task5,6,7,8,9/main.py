from collections.courier_company_collection import CourierCompanyCollection
from services.courier_user_service_collection_impl import CourierUserServiceCollectionImpl
from services.courier_admin_service_collection_impl import CourierAdminServiceCollectionImpl
from entities.courier import Courier
from entities.employee import Employee
import sys

def main():
    # Initialize the courier company
    company_obj = CourierCompanyCollection("FastExpress")
    
    # Create service implementations for user and admin
    user_service = CourierUserServiceCollectionImpl(company_obj)
    admin_service = CourierAdminServiceCollectionImpl(company_obj)
    
    while True:
        print("\n=== Courier Management System ===")
        print("1. Place a Courier Order")
        print("2. Get Courier Order Status")
        print("3. Cancel a Courier Order")
        print("4. Add Courier Staff (Admin)")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            # Place an order
            sender_name = input("Enter sender name: ")
            sender_address = input("Enter sender address: ")
            receiver_name = input("Enter receiver name: ")
            receiver_address = input("Enter receiver address: ")
            weight = float(input("Enter parcel weight: "))
            user_id = int(input("Enter your user ID: "))

            # Create a new Courier object
            courier = Courier(
                sender_name=sender_name, 
                sender_address=sender_address,
                receiver_name=receiver_name, 
                receiver_address=receiver_address, 
                weight=weight, 
                user_id=user_id
            )

            tracking_number = user_service.place_order(courier)
            print(f"Order placed successfully! Your tracking number is {tracking_number}")

        elif choice == '2':
            # Get courier order status
            tracking_number = int(input("Enter tracking number: "))
            try:
                status = user_service.get_order_status(tracking_number)
                print(f"The current status of the order with tracking number {tracking_number} is: {status}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            # Cancel an order
            tracking_number = int(input("Enter tracking number to cancel: "))
            try:
                success = user_service.cancel_order(tracking_number)
                if success:
                    print("Order canceled successfully.")
                else:
                    print("Failed to cancel the order.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            # Add courier staff (admin functionality)
            employee_id = int(input("Enter employee ID: "))  # Get employee ID from user input
            employee_name = input("Enter employee name: ")
            email = input("Enter employee email: ")
            contact_number = input("Enter employee contact number: ")
            role = input("Enter employee role: ")
            salary = float(input("Enter employee salary: "))

            employee = Employee(
                employee_id=employee_id,  # Set employee ID from input
                employee_name=employee_name, 
                email=email, 
                contact_number=contact_number, 
                role=role, 
                salary=salary
            )

            try:
                added_employee_id = admin_service.add_courier_staff(employee)
                print(f"Employee added successfully! Employee ID is {added_employee_id}")
            except Exception as e:
                print(f"Error: {e}")


        elif choice == '5':
            # Exit the program
            print("Exiting the system. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
