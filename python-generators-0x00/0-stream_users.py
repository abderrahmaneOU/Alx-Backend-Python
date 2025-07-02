#!/usr/bin/python3
import mysql.connector

def stream_users():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",  # change this to your actual MySQL root password
        database="ALX_prodev"
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row

    cursor.close()
    connection.close()
