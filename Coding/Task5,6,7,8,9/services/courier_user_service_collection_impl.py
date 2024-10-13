from services.icourier_user_service import ICourierUserService
from exceptions.tracking_number_not_found_exception import TrackingNumberNotFoundException
from collections.courier_company_collection import CourierCompanyCollection

class CourierUserServiceCollectionImpl(ICourierUserService):
    def __init__(self, company_obj: CourierCompanyCollection):
        self.company_obj = company_obj

    def place_order(self, courier_obj):
        """Place a new courier order"""
        self.company_obj.add_courier(courier_obj)
        return courier_obj.get_tracking_number()

    def get_order_status(self, tracking_number):
        """Get the status of a courier order by tracking number"""
        for courier in self.company_obj.courier_details:
            if courier.get_tracking_number() == tracking_number:
                return courier.status
        raise TrackingNumberNotFoundException(tracking_number)

    def cancel_order(self, tracking_number):
        """Cancel an existing courier order"""
        for courier in self.company_obj.courier_details:
            if courier.get_tracking_number() == tracking_number:
                self.company_obj.courier_details.remove(courier)
                return True
        raise TrackingNumberNotFoundException(tracking_number)

    def get_assigned_order(self, courier_staff_id):
        """Get a list of orders assigned to a specific courier staff member"""
        assigned_orders = [
            courier for courier in self.company_obj.courier_details
            if courier.user_id == courier_staff_id
        ]
        return assigned_orders
