import mysql.connector
import sys

# Approach 2
# Used random to reduce probability of booking same seat again.
# Did not check whether seat is assigned or not, same seat can be booked again.


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
def book_seat(connection, user_id, booking_id):
    cursor = connection.cursor()
    connection.commit()

    # Update the booking to set the user ID.
    try:
        connection.start_transaction()
        cursor.execute(f"Update booking set user_id={user_id} where id={booking_id}")
        connection.commit()
    except mysql.connector.Error as err:
        connection.rollback()
        print("Error Occured:", err)


# This is the main function.
def main():
    # Connect to the database.
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute("update booking set user_id=null")
    connection.commit()

    # Get the user ID from the command line arguments.
    user_id = sys.argv[1]

    # Get username
    query = "Select name from USER where user_id=%s"
    cursor.execute(query, (user_id,))
    user_name = cursor.fetchone()[0]
    connection.commit()
    print(f"Hi {user_name}!")

    # Get seat id
    cursor.execute("SELECT id, seat_id FROM booking ORDER BY RAND() LIMIT 1;")
    result = cursor.fetchone()
    booking_id, seat_id = result[0], result[1]
    connection.commit()

    # Try to book the seat.
    try:
        book_seat(connection, user_id, booking_id)
        print(f"Booked seat {seat_id} for you")
    except mysql.connector.Error as err:
        print("Error Occured:", err)

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

    # Close the database connection.
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
