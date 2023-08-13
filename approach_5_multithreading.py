import mysql.connector
import threading
import time


# Approach 5 using multithreading
# This function connects to a MySQL database.
def connect_to_database():
    # Connect to the database using the specified credentials.
    connection = mysql.connector.connect(
        host='localhost',
        user="root",
        password="bwell@123",
        database="corona_db"
    )
    return connection


# This function books a seat in the database.
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

    # Update the booking to set the user ID.
    try:
        # Get seat id
        cursor.execute("SELECT id, seat_id FROM booking where session_id=1 and user_id is null order by "
                       "id limit 1 FOR UPDATE SKIP LOCKED")
        result = cursor.fetchone()
        seat_id = result[1]
        booking_id = result[0]

        # Update the booking to set the user ID.
        query = "Update booking set user_id=%s where id = %s"
        cursor.execute(query, (user_id, booking_id,))
        connection.commit()
        print(f"Booked seat {seat_id} for you {user_name}")
    except mysql.connector.Error as err:
        connection.rollback()
        print("Error:", err)
        print("Restarting")

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
        threads.append(thread)
        thread.start()

    # Wait for all processes to finish
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
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.5f} seconds")
