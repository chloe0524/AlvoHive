#!/usr/bin/env python3
import psycopg2
from psycopg2 import Error
import mdutils
import requests

db_params = {
    "host": "localhost",
    "port": 5432,
    "database": "alvo_db",
    "user": "alvo",
    "password": "alvo"
}

def execute_query_and_write_to_md(query, headers, mdFile):
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.extend(list(row))
        mdFile.new_table(columns=len(headers), rows=len(data)//len(headers)+1, text=headers+data, text_align='center')
        cursor.close()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            connection.close()

def fetch_cpe_and_query_api(mdFile):
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute("SELECT cpe FROM service_version WHERE id_hosts=1")
        cpes = cursor.fetchall()
        
        for cpe_row in cpes:
            cpe = cpe_row[0]
            url = f"https://localhost:8443/api/cvefor/{cpe}"
            headers = {
                'X-Api-Key': 'f06b8e71-9eda-46e5-9dd9-1b73d18440ce'
            }
            response = requests.get(url, headers=headers, verify=False)
            cves = response.json()  # parse the response as JSON
            
            for cve in cves:
                # Write the CVE summary and cvss to the markdown file
                mdFile.new_paragraph(f"--> CVE for {cpe}:")
                mdFile.new_paragraph(f"Summary: {cve['summary']}")
                mdFile.new_paragraph(f"CVSS: {cve['cvss']}")
                mdFile.new_paragraph("---")  # Add a horizontal line
        
        cursor.close()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            connection.close()

mdFile = mdutils.MdUtils(file_name='r', title='Query Results')

query1 = """
    SELECT company_name, first_name, last_name
    FROM company, contact
    WHERE contact.last_name = 'Doe'
"""
headers1 = ["Company Name", "First Name", "Last Name"]
execute_query_and_write_to_md(query1, headers1, mdFile)

query2 = """
    SELECT name, os_name, os_sp
    FROM hosts, service_version
    WHERE id=id_hosts AND id_hosts=1
    LIMIT 1
"""
headers2 = ["Name", "OS Name", "OS SP"]
execute_query_and_write_to_md(query2, headers2, mdFile)

query3 = """
    SELECT cpe
    FROM service_version
    WHERE id_hosts=1
"""
headers3 = ["CPE"]
execute_query_and_write_to_md(query3, headers3, mdFile)

fetch_cpe_and_query_api(mdFile)

mdFile.create_md_file()
