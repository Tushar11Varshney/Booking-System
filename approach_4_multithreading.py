import mysql.connector
import threading


# Approach 4 using multithreading
# This function connects to a MySQL database.
def connect_to_database():
    # Connect to the database using the specified credentials.
    connection = mysql.connector.connect(
        host='localhost',
        user="root",
        password="xxxxxxx",
        database="corona_db"
    )
    return connection


def book_seat(user_id):
    # Connect to the database.
    connection = connect_to_database()
    cursor = connection.cursor()

    # Get username
    query = "Select name from USER where user_id=%s"
    cursor.execute(query, (user_id,))
    user_name = cursor.fetchone()[0]
    connection.commit()
    print(f"Hi {user_name}!")

    # Get seat id
    with threading.Lock():
        cursor.execute("SELECT id, seat_id FROM booking where user_id is null and session_id=1 limit 1")
        result = cursor.fetchone()
        booking_id, seat_id = result[0], result[1]
    connection.commit()

    # Update the booking to set the user ID.
    try:
        connection.start_transaction()
        query = "Update booking set user_id=%s where id = %s"
        cursor.execute(query, (user_id, booking_id,))
        connection.commit()
    except mysql.connector.Error as err:
        connection.rollback()
        print("Error Occurred:", err)

    print(f"Booked seat {seat_id} for you {user_name}")
    cursor.close()
    connection.close()


# This is the main function.
def main():

    # Connect to the database.
    connection = connect_to_database()
    cursor = connection.cursor()

    # Clear database
    cursor.execute("update booking set user_id=null")
    connection.commit()

    # Create and start a thread for each user
    threads = []
    for user_id in range(1, 121):
        thread = threading.Thread(target=book_seat, args=(user_id,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    cursor.execute("Select seat_id, user_id from booking")
    result = dict(cursor.fetchall())
    connection.commit()

    for i in range(10, 0, -1):
        for j in range(ord('A'), ord('M')):
            if result[f"{i}-{chr(j)}"]:
                print("X", end="  ")
            else:
                print(".", end="  ")
        print()


if __name__ == "__main__":
    main()
