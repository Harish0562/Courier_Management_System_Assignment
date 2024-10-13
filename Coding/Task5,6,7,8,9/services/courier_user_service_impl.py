from services.icourier_user_service import ICourierUserService
from exceptions.tracking_number_not_found_exception import TrackingNumberNotFoundException

class CourierUserServiceCollectionImpl(ICourierUserService):
    def __init__(self, company_obj):
        self.company_obj = company_obj

    def place_order(self, courier_obj):
        self.company_obj.add_courier(courier_obj)
        return courier_obj.get_tracking_number()

    def get_order_status(self, tracking_number):
        courier = self.get_courier_by_tracking_number(tracking_number)  # Implement this method to get the courier object

        if courier:
            return courier.get_status()  # Use the getter method
        else:
            raise Exception(f"Tracking number {tracking_number} not found.")

    def cancel_order(self, tracking_number):
        for courier in self.company_obj.courier_details:
            if courier.get_tracking_number() == tracking_number:
                self.company_obj.courier_details.remove(courier)
                return True
        raise TrackingNumberNotFoundException(tracking_number)

    def get_assigned_order(self, courier_staff_id):
        return [courier for courier in self.company_obj.courier_details if courier.user_id == courier_staff_id]
