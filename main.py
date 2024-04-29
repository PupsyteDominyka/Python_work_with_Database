
import mysql.connector

import mysql.connector
conn = mysql.connector.connect

hostname = "localhost"
username = "root"
password = ""
database = "sakila"
portAddress= 3306

connection = None
cursor = None

try:
    connection = mysql.connector.connect(host=hostname, user=username, password=password, database=database, port=portAddress)
    print("Connection successful!")

    cursor = connection.cursor()
    query = "SELECT * FROM actor"
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Surname: {row[2]} ")

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Connection closed.")

#atvaizduoti visus customerius
# atvaizduoti visus customerius ir stulpelį kuriame būtų atvaizduota kiek pinigų kiekvienas jų yra išleidęs nuomai, ir kiek filmų nuomavesis
# atvaizduoti aktorius ir keliuose filmuose jie yra filmavesi
# atvaizduoti visus filmus ir kiek aktorių juose vaidino
# su pitono pagalba: nustatyti kuris nuomos punktas:
#--turi daugiau customerių
#--išnuomavo daugiau(ir kiek kiekvienas) filmų
#--kiek sugeneravo pajamų

print("---------------------------------------2----------------------------------------")
# atvaizduoti visus customerius ir stulpelį kuriame būtų atvaizduota kiek pinigų kiekvienas jų yra išleidęs nuomai, ir kiek filmų nuomavesis

import mysql.connector

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

print("Customer ID | Full Name          | Total Rentals | Total Amount Spent")
for row in result:
    customer_id, full_name, total_rentals, total_amount_spent = row
    print(f"{customer_id:11} | {full_name:20} | {total_rentals:13} | {total_amount_spent:18}")

cursor.close()
conn.close()

print("---------------------------------------3----------------------------------------")
# atvaizduoti aktorius ir keliuose filmuose jie yra filmavesi

import mysql.connector
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

print("Actor ID | Actor Name          | Number of Films")
for row in result:
    actor_id, actor_name, num_films = row
    print(f"{actor_id:8} | {actor_name:20} | {num_films:15}")

cursor.close()
conn.close()

print("---------------------------------------4----------------------------------------")
# atvaizduoti visus filmus ir kiek aktorių juose vaidino

import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sakila"
)
cursor = conn.cursor()
query = """
    SELECT 
        f.film_id, 
        f.title AS film_title, 
        COUNT(fa.actor_id) AS num_actors
    FROM 
        film f
    JOIN 
        film_actor fa ON f.film_id = fa.film_id
    GROUP BY 
        f.film_id, f.title
    ORDER BY 
        num_actors DESC
"""
cursor.execute(query)
result = cursor.fetchall()

print("Film ID | Film Title                    | Number of Actors")
for row in result:
    film_id, film_title, num_actors = row
    print(f"{film_id:8} | {film_title:30} | {num_actors:15}")

cursor.close()
conn.close()

print("---------------------------------------5----------------------------------------")
# su pitono pagalba: nustatyti kuris nuomos punktas:
#--turi daugiau customerių
#--išnuomavo daugiau(ir kiek kiekvienas) filmų
#--kiek sugeneravo pajamų

import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sakila"
)
cursor = conn.cursor()
query = """
    SELECT 
        s.store_id, 
        a.address AS store_address, 
        COUNT(DISTINCT c.customer_id) AS num_customers, 
        COUNT(DISTINCT r.rental_id) AS num_rentals, 
        SUM(p.amount) AS total_revenue
    FROM 
        store s
    LEFT JOIN 
        address a ON s.address_id = a.address_id
    LEFT JOIN 
        customer c ON s.store_id = c.store_id
    LEFT JOIN 
        rental r ON c.customer_id = r.customer_id
    LEFT JOIN 
        payment p ON r.rental_id = p.rental_id
    GROUP BY 
        s.store_id, a.address
    ORDER BY 
        num_customers DESC, num_rentals DESC, total_revenue DESC
    LIMIT 
        1
"""
cursor.execute(query)
result = cursor.fetchone()

if result:
    store_id, store_address, num_customers, num_rentals, total_revenue = result
    print("Store ID:", store_id)
    print("Store Address:", store_address)
    print("Number of Customers:", num_customers)
    print("Number of Rentals:", num_rentals)
    print("Total Revenue:", total_revenue)
else:
    print("No data found for stores.")

cursor.close()
conn.close()

