class Location:
    def __init__(self, location_id=None, location_name=None, address=None):
        self.__location_id = location_id
        self.__location_name = location_name
        self.__address = address

    def __str__(self):
        return f"Location [ID={self.__location_id}, Name={self.__location_name}]"
