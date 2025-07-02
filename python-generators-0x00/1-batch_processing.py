import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator to yield users in batches of batch_size"""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # <-- Use your MySQL password if any
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)

    offset = 0
    while True:
        cursor.execute(
            "SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset)
        )
        rows = cursor.fetchall()
        if not rows:
            break
        yield rows
        offset += batch_size

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """Process and print users over the age of 25 from each batch"""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
