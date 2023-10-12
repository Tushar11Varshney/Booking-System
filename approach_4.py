import mysql.connector
import multiprocessing


# Approach 4 using multiprocessing
# All 120 user came at same time, checked if seat is null. Will all seats be filled?
# This function connects to a MySQL database.
def connect_to_database():
    # Connect to the database using the specified credentials.
    connection = mysql.connector.connect(
        host='localhost',
        user="root",
        password="xxxxxx",
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

    # Get seat id
    cursor.execute("SELECT id, seat_id FROM booking where user_id is null and session_id=1 limit 1")
    result = cursor.fetchone()
    print(f"=============={result}=======")
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
        print("Error Occured:", err)

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
    main()
