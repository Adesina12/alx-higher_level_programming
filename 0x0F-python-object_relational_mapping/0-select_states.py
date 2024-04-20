#!/usr/bin/python3
'''Select States'''
import mysql.connector
from mysql.connector import Error
import sys
import MySQLdb

try:
    connection = mysql.connector.connect(
            user=sys.argv[1],
            host='localhost',
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306,
            )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM states;')
        record = (cursor.fetchall())
        for num in record:
            print(num)

except Error as e:
    print("The Error is ", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
