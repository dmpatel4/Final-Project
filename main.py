
import mysql.connector  # Import connector to access sql database
from mysql.connector import Error  # Import error to make sure connection is successful

# Create a function to connect to the sql database using mysql connector
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            # Input details such as host, username, password, and database name to connect
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        # If connection is successful display success message to use
        print("Connection to MySQL DB successful.\n")
    except Error as e:
        # If input details are incorrect and connection is not successfull display error message.
        print(f"The error '{e}' occurred")

    return connection


# Create a function to execute an insert query to the successfully connected mysql database
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        # Display success message if the query is executed
        print("Query executed successfully.\n")
    except Error as e:
        # Display error message if details do not match and query does not execute
        print(f"The error '{e}' occurred")


# Create a function to execute an insert query to the successfully connected mysql database
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create_connection("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
