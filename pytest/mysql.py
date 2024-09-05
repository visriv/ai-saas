import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection to the server (without specifying a database)
    connection = mysql.connector.connect(
        host='database-1.cxuwyeay0ss4.us-east-2.rds.amazonaws.com',
        port=3306,
        user='admin',
        password='134679vs',  # Replace with your actual password,
        database='db1'  # Replace with your database name

    )

    if connection.is_connected():
        print("Connected to MySQL server")

        # Create a cursor object using the connection
        cursor = connection.cursor()

        # Execute a query to show all databases
        cursor.execute("SHOW DATABASES")

        # Fetch all results from the executed query
        databases = cursor.fetchall()

        print("Databases on the server:")
        for db in databases:
            print(db[0])

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()  # Close the cursor
        connection.close()  # Close the connection
        print("MySQL connection is closed")
