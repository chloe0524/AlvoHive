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
        mdFile.new_table(columns=len(headers), rows=len(data)//len(headers)+1, text=headers+data, text_align='left')
        cursor.close()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            connection.close()

def fetch_cpe_and_query_api(mdFile):
    data = []  # Initialize data
    details = []  # Initialize details
    first_cve = True  # Initialize first_cve to True

    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute("SELECT cpe FROM service_version WHERE id_hosts=1")
        cpes = cursor.fetchall()
        
        for cpe_row in cpes:
            cpe = cpe_row[0]
            url = f"https://localhost:8443/api/cvefor/{cpe}"
            headers = {
                'X-Api-Key': 'beea668b-e1fb-48b6-a279-3f96073de90f'
            }
            response = requests.get(url, headers=headers, verify=False)
            cves = response.json()  # parse the response as JSON
            
            for cve in cves:
                try:
                    cvss = float(cve.get('cvss', 0))  # Get CVSS and default to 0 if not found
                    if cvss >= 9.0:
                        data.append([cve['id'], cvss])  # Add to data list
                except Exception as e:
                    print(f"Error processing CVE data: {e}")
                
                if first_cve:
                    details.append("\n## Details\n")  # Add a newline before the "Details" title
                    first_cve = False
                details.append(f"## {cve.get('id', 'Unknown ID')}\n")
                details.append(f"--> CVE for {cpe} ({cve.get('id', 'Unknown ID')}):\n")
                details.append(f"Summary: {cve.get('summary', 'No summary available')}\n")
                details.append(f"CVSS: {cve.get('cvss', 'N/A')}\n")
        
        cursor.close()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            connection.close()

    if data:  # Only create the table if there is data
        headers = ["CVE", "Critical Severity"]
        mdFile.new_table(columns=2, rows=len(data)+1, text=headers+sum(data, []), text_align='left')
    
    return details

mdFile = mdutils.MdUtils(file_name='report')

# Fetch CVE data and query API
mdFile.new_header(level=1, title="WARNING:")
details_section = fetch_cpe_and_query_api(mdFile)

# Execute and write other queries to markdown file
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

mdFile.create_md_file()

# Combine the markdown content with details section at the end
with open('report.md', 'a') as md_file:
    md_file.write("\n".join(details_section))
