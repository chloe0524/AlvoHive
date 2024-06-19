#!/usr/bin/env python3
import psycopg2
from psycopg2 import Error
import mdutils

# Database connection parameters
db_params = {
    "host": "localhost",
    "port": 5432,
    "database": "alvo_db",
    "user": "alvo",
    "password": "alvo"
}

def execute_query_and_write_to_md(query, headers, mdFile):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**db_params)
        
        # Create a cursor object using the connection
        cursor = connection.cursor()
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch all rows from the result set
        rows = cursor.fetchall()
        
        # Add each row to the markdown file
        data = []
        for row in rows:
            data.extend(list(row))
        
        # Write the table to the markdown file
        mdFile.new_table(columns=len(headers), rows=len(data)//len(headers)+1, text=headers+data, text_align='center')
        
        # Close communication with the database
        cursor.close()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # Finally, close the database connection
        if connection:
            connection.close()

# Create a markdown file
mdFile = mdutils.MdUtils(file_name='Output', title='Query Results')

# Execute the first query
query1 = """
    SELECT company_name, first_name, last_name
    FROM company, contact
    WHERE contact.last_name = 'Doe'
"""
headers1 = ["Company Name", "First Name", "Last Name"]
execute_query_and_write_to_md(query1, headers1, mdFile)

# Execute the second query
query2 = """
    SELECT name, os_name, os_sp
    FROM hosts, service_version
    WHERE id=id_hosts AND id_hosts=1
    LIMIT 1
"""
headers2 = ["Name", "OS Name", "OS SP"]
execute_query_and_write_to_md(query2, headers2, mdFile)

# Execute the third query
query3 = """
    SELECT cpe
    FROM service_version
    WHERE id_hosts=1
"""
headers3 = ["CPE"]
execute_query_and_write_to_md(query3, headers3, mdFile)

# Create the markdown file
mdFile.create_md_file()