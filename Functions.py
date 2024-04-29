import mysql.connector
def fetch_actors():
    hostname = "localhost"
    username = "root"
    password = ""
    database = "sakila"
    portAddress = 3306

    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(host=hostname, user=username, password=password, database=database, port=portAddress)
        print("Connection successful!")
        cursor = connection.cursor()
        query = "SELECT * FROM actor"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Connection closed.")
actors = fetch_actors()
if actors:
    for row in actors:
        print(f"ID: {row[0]}, Name: {row[1]}, Surname: {row[2]} ")

