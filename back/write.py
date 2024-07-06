#!/usr/bin/python3

import subprocess
import os
import psycopg2
from psycopg2 import Error
import mdutils
import requests
import os

host_id=2

# Database parameters
db_params = {
    "host": "localhost",
    "port": 5432,
    "database": "alvo_db",
    "user": "alvo",
    "password": "alvo"
}

# Function to execute query and write to markdown
def execute_query_and_write_to_md(query, headers, mdFile):
    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute(query,(host_id))
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

# Function to fetch CPE and query API for CVE data
def fetch_cpe_and_query_api(mdFile):
    there_is_data = []
    details = []
    first_cve = True 

    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute("SELECT cpe FROM service_version WHERE id_hosts="+str(host_id))
        cpes = cursor.fetchall()
        
        for cpe_row in cpes:
            cpe = cpe_row[0]
            url = f"https://localhost:8443/api/cvefor/{cpe}"
            headers = {
                'X-Api-Key': 'key'
            }
            response = requests.get(url, headers=headers, verify=False)
            cves = response.json()
            
            for cve in cves:
                try:
                    cvss = float(cve.get('cvss', 0))
                    if cvss >= 8.9:
                        there_is_data.append([f"[CVE-{cve['id']}](#{cve['id']})", f"<span style='color:red;'>{cvss}</span>"])
                    if first_cve:
                        details.append("\n# Details\n")
                        first_cve = False
                    details.append(f"## {cve.get('id', 'Unknown ID')}\n")
                    details.append(f" !--> CVE for {cpe}\n")
                    details.append(f"Summary: {cve.get('summary', 'No summary available')}\n")
                    details.append(f"\n\n\\textbf{{\\textcolor{{red}}{{CVSS: {cve.get('cvss', 'N/A')}}}}}\n\n")
                except Exception as e:
                    print(f"Error processing CVE data: {e}")
        
        cursor.close()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            connection.close()

    if there_is_data:
        headers = ["CVE", "Critical Severity"]
        mdFile.new_table(columns=2, rows=len(there_is_data)+1, text=headers+sum(there_is_data, []), text_align='left')
    
    return details


# Main begins



mdFile = mdutils.MdUtils(file_name='report', title='')

# Query for company and contact information
query1 = "SELECT company_name, first_name, last_name FROM report WHERE id="+str(host_id)

headers1 = ["Company Name", "First Name", "Last Name"]
execute_query_and_write_to_md(query1, headers1, mdFile)

# Query for host and service version information
query2 = "SELECT name, os_name, os_sp FROM hosts WHERE hosts.id="+str(host_id)
    
headers2 = ["Name", "OS Name", "OS SP"]
execute_query_and_write_to_md(query2, headers2, mdFile)

# Fetch CVE data and process it
details_section = fetch_cpe_and_query_api(mdFile)


# Finalize markdown file
mdFile.create_md_file()

# Append additional details to the markdown file
with open('report.md', 'a') as md_file:
    md_file.write("\n".join(details_section))

# Convert markdown to PDF and run additional scripts
subprocess.run(['pandoc', 'reports/report.md', '-o', 'reports/report.pdf', '--template=template.tex', '--pdf-engine=lualatex'])
subprocess.run(['./bar_chart.py'])
subprocess.run(['./pie_graphic.py'])

if __name__ == "__main__":
    host_id=5