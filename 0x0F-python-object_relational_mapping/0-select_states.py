#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""

import mysql.connector
from mysql.connector import Error
import sys
"""python3 -c 'print(__import__("my_module").__doc__)'"""

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

if connection.is_connected():
    cursor.close()
    connection.close()
