import sqlite3

# Create connection method (Creates databse if already doesnt exists)
def create_connection(database):
    connection = None
    try:
        connection = sqlite3.connect(database)
        print("Connection to DB successful")
    except:
        print("Error connecting to database")

    return connection

def close_connection(connection):
    connection.close()

    
# Execute query method
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except:
        print("Error excuting the query")


# Read query method
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Reading Query Successful")
        return result
    except:
        print("Error Reading the query")