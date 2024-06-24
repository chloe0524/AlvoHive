#!/usr/bin/python3
 
#
# Update the logo for a company
#

import os
import sys
import psycopg2

def update_logo(file_path, image_id):
	try:
		conn = psycopg2.connect("host='localhost' dbname='alvo_db' user='alvo' password='alvo' port=5432")
	except ConnectionError as err:
		print("PostgreSQL connection failed")
	
	cur = conn.cursor()

	# Check if the file exists and is a png
	if os.path.isfile(file_path) and file_path.lower().endswith(('.png')):
		with open(file_path, 'rb') as file:
			binary_data = file.read()

			# Update logo for the row indentified with the specified ID
			cur.execute(f"UPDATE company SET logo=%s WHERE id_company=%s", (psycopg2.Binary(binary_data), image_id))  
	
		conn.commit()

		print(f"Logo {file_path} updated for company ID {image_id}.")
	else:
		print(f"File {file_path} does not exist or is not a png.")

	cur.close()
	conn.close()

if len(sys.argv) != 3:
    print("Usage: python populate_company_logo.py <logo file> <company id>")
    sys.exit(1)

file_path = sys.argv[1]
image_id = int(sys.argv[2])

update_logo(file_path, image_id)

