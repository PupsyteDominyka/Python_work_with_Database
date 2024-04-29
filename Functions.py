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


def fetch_customer_data():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sakila"
        )
        cursor = conn.cursor()

        query = """
            SELECT 
                c.customer_id, 
                CONCAT(c.first_name, ' ', c.last_name) AS full_name, 
                COUNT(p.rental_id) AS total_rentals,
                SUM(p.amount) AS total_amount_spent
            FROM 
                customer c
            LEFT JOIN 
                payment p ON c.customer_id = p.customer_id
            GROUP BY 
                c.customer_id, c.first_name, c.last_name
            ORDER BY 
                total_amount_spent DESC
        """
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            print("Customer ID | Full Name          | Total Rentals | Total Amount Spent")
            for row in result:
                customer_id, full_name, total_rentals, total_amount_spent = row
                print(f"{customer_id:11} | {full_name:20} | {total_rentals:13} | {total_amount_spent:18}")
        else:
            print("No data found for customers.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

fetch_customer_data()

def fetch_actor_data():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sakila"
        )
        cursor = conn.cursor()

        query = """
            SELECT 
                a.actor_id, 
                CONCAT(a.first_name, ' ', a.last_name) AS actor_name, 
                COUNT(fa.film_id) AS num_films
            FROM 
                actor a
            JOIN 
                film_actor fa ON a.actor_id = fa.actor_id
            GROUP BY 
                a.actor_id, a.first_name, a.last_name
            ORDER BY 
                num_films DESC
        """
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            print("Actor ID | Actor Name          | Number of Films")
            for row in result:
                actor_id, actor_name, num_films = row
                print(f"{actor_id:8} | {actor_name:20} | {num_films:15}")
        else:
            print("No data found for actors.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn:
            conn.close()

fetch_actor_data()


