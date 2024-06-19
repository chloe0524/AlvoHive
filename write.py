#!/usr/bin/env python3
import psycopg2
from psycopg2 import Error
import mdutils

# Database connection
db_params = {
    "host": "localhost",
    "port": 5432,
    "database": "alvo_db",
    "user": "alvo",
    "password": "alvo"
}

def execute_query_and_write_to_md(query, headers, mdFile, column_widths):
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.extend([str(item).ljust(width) for item, width in zip(row, column_widths)])
        
        mdFile.new_line('-----------------')
        mdFile.new_line(headers[0])
        mdFile.new_line('-----------------')
        mdFile.new_table(columns=len(headers), rows=len(data)//len(headers)+1, text=headers+data, text_align='left')
        
        cursor.close()

    except (Exception, Error) as error:
        print("ça marche pas démerde-toi", error)

    finally:
        # close connection to database
        if connection:
            connection.close()

def remove_table_separators(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            if not line.strip().startswith('| :---'):
                file.write(line)

mdFile = mdutils.MdUtils(file_name='r', title='Data from queries')

query1 = """
    SELECT company_name, first_name, last_name
    FROM company, contact
    WHERE contact.last_name = 'Doe'
"""
headers1 = ["Company Name".ljust(20), "First Name".ljust(20), "Last Name".ljust(20)]
column_widths1 = [20, 20, 20]
execute_query_and_write_to_md(query1, headers1, mdFile, column_widths1)

query2 = """
    SELECT name, os_name, os_sp
    FROM hosts, service_version
    WHERE id=id_hosts AND id_hosts=1
    LIMIT 1
"""
headers2 = ["Name".ljust(20), "OS Name".ljust(20), "OS SP".ljust(20)]
column_widths2 = [20, 20, 20]
execute_query_and_write_to_md(query2, headers2, mdFile, column_widths2)

query3 = """
    SELECT cpe
    FROM service_version    WHERE id_hosts=1
"""
headers3 = ["CPE".ljust(20)]
column_widths3 = [20]
execute_query_and_write_to_md(query3, headers3, mdFile, column_widths3)

mdFile.create_md_file()
remove_table_separators('r.md')