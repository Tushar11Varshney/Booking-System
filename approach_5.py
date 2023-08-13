import mysql.connector
import multiprocessing
import time

# Approach 5 using multiprocessing
# Skip lock and exclusive lock
# All 120 user came at same time, checked if seat is null. will first user get first seat?


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

    num_attempts = 3
    while num_attempts > 0:
        try:
            # Get seat id
            cursor.execute(
                "SELECT id, seat_id FROM booking where session_id=1 and user_id is null order by id limit 1"
                " FOR UPDATE"
            )
            result = cursor.fetchone()
            seat_id = result[1]
            booking_id = result[0]

            # Update the booking to set the user ID.
            query = "Update booking set user_id=%s where id = %s"
            cursor.execute(query, (user_id, booking_id,))
            connection.commit()
            print(f"Booked seat {seat_id} for you {user_name}")
            break
        except mysql.connector.Error as err:
            connection.rollback()
            print("Error:", err)
            print("Restarting")
            num_attempts -= 1
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

    # Create and start a process for each user
    processes = []
    for user_id in range(1, 121):
        process = multiprocessing.Process(target=book_seat, args=(user_id,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

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
