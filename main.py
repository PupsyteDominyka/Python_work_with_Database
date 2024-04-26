
import mysql.connector

import mysql.connector

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
    query = "SELECT * FROM actor"  # Replace with your desired query
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Surname: {row[2]}")  # Access column data by index

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
