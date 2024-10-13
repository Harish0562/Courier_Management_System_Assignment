# entities/courier.py
class Courier:
    tracking_number_counter = 1000  # Static variable for tracking number

    def __init__(self, sender_name, sender_address, receiver_name, receiver_address, weight, user_id):
        self.__tracking_number = Courier.tracking_number_counter  # Generate a unique tracking number
        Courier.tracking_number_counter += 1  # Increment for the next order
        self.__sender_name = sender_name
        self.__sender_address = sender_address
        self.__receiver_name = receiver_name
        self.__receiver_address = receiver_address
        self.__weight = weight
        self.__status = "yetToTransit"  # Initialize status
        self.__user_id = user_id

    # Getter for tracking number
    def get_tracking_number(self):
        return self.__tracking_number

    # Other getters and setters...
    def get_sender_name(self):
        return self.__sender_name

    def get_sender_address(self):
        return self.__sender_address

    def get_receiver_name(self):
        return self.__receiver_name

    def get_receiver_address(self):
        return self.__receiver_address

    def get_weight(self):
        return self.__weight

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_user_id(self):
        return self.__user_id

    def __str__(self):
        return f"Courier(Tracking Number: {self.__tracking_number}, Sender: {self.__sender_name}, Receiver: {self.__receiver_name}, Status: {self.__status})"
