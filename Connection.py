import mysql.connector

# Replace these values with your actual database credentials
db_config = {
    'host': '192.168.85.23',
    'user': 'sammy',
    'password': 'password',
    'database': 'network_scan15'
}

# Connect to the database
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Define the query to fetch data from the table
    query = "SELECT id, timestamp, ip_address, result FROM scan_results"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Print the column headers
    print("ID\tTimestamp\tIP Address\tResult")

    # Print the fetched data
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")