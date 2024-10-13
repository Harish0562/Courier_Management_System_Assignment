import pyodbc
from connectionutil.db_connection import DBConnection
from entities.courier import Courier
from entities.payment import Payment

class CourierServiceDb:
    def __init__(self):
        self.connection = DBConnection.get_connection()

    def insert_order(self, courier_obj):
        cursor = self.connection.cursor()
        query = """INSERT INTO Courier (sender_name, sender_address, receiver_name, receiver_address, weight, status, tracking_number, user_id) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (courier_obj.sender_name, courier_obj.sender_address, courier_obj.receiver_name,
                               courier_obj.receiver_address, courier_obj.weight, courier_obj.status, 
                               courier_obj.get_tracking_number(), courier_obj.user_id))
        self.connection.commit()

    def update_order_status(self, tracking_number, new_status):
        cursor = self.connection.cursor()
        query = """UPDATE Courier SET status = ? WHERE tracking_number = ?"""
        cursor.execute(query, (new_status, tracking_number))
        self.connection.commit()

    def get_delivery_history(self, tracking_number):
        cursor = self.connection.cursor()
        query = """SELECT * FROM Courier WHERE tracking_number = ?"""
        cursor.execute(query, (tracking_number,))
        return cursor.fetchone()

    def generate_report(self):
        cursor = self.connection.cursor()
        query = """SELECT status, COUNT(*) as count FROM Courier GROUP BY status"""
        cursor.execute(query)
        return cursor.fetchall()

    def generate_revenue_report(self):
        cursor = self.connection.cursor()
        query = """SELECT SUM(Amount) as total_revenue FROM Payment"""
        cursor.execute(query)
        return cursor.fetchone()
