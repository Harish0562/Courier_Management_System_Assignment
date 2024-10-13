class Payment:
    def __init__(self, payment_id=None, courier_id=None, amount=None, payment_date=None):
        self.__payment_id = payment_id
        self.__courier_id = courier_id
        self.__amount = amount
        self.__payment_date = payment_date

    def __str__(self):
        return f"Payment [ID={self.__payment_id}, Amount={self.__amount}]"
