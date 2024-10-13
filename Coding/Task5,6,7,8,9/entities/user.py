class User:
    def __init__(self, user_id=None, user_name=None, email=None, password=None, contact_number=None, address=None):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__email = email
        self.__password = password
        self.__contact_number = contact_number
        self.__address = address

    # Getters
    def get_user_id(self):
        return self.__user_id

    def get_user_name(self):
        return self.__user_name

    # Setters
    def set_user_name(self, user_name):
        self.__user_name = user_name

    # __str__ method
    def __str__(self):
        return f"User [ID={self.__user_id}, Name={self.__user_name}, Email={self.__email}]"
