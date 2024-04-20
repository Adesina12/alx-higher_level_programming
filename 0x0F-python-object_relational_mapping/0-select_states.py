#!/usr/bin/python3
"""Select States"""

import mysql.connector
from mysql.connector import Error
import sys
import MySQLdb

try:
    """Try this"""
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
    """except this"""
    print("The Error is ", e)
finally:
    """Finally this"""
    if connection.is_connected():
        cursor.close()
        connection.close()
