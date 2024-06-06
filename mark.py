#!/usr/bin/python3
import requests
from mdutils.mdutils import MdUtils

BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

cve_ids = [
    "CVE-2024-35655",
    "CVE-2024-35664", 
    "CVE-2024-35666",
    "CVE-2024-35668"
]

mdFile = MdUtils(file_name='cve_report', title='CVE Report')

for cve_id in cve_ids:
    url = f"{BASE_URL}?cveId={cve_id}"

    response = requests.get(url)

    if response.status_code == 200:
        cve_data = response.json()

        if cve_data["totalResults"] > 0:
            cve_description = cve_data["vulnerabilities"][0]["cve"]["descriptions"][0]["value"]
            
            if "cvssMetricV3" in cve_data["vulnerabilities"][0]["cve"]["metrics"]:
                cve_severity = cve_data["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV3"]["cvssData"]["baseSeverity"]
            elif "cvssMetricV2" in cve_data["vulnerabilities"][0]["cve"]["metrics"]:
                cve_severity = cve_data["vulnerabilities"][0]["cve"]["metrics"]["cvssMetricV2"]["cvssData"]["baseSeverity"]
            else:
                cve_severity = "Not available"

            mdFile.new_line()
            mdFile.new_header(level=1, title=f"CVE ID: {cve_id}")
            mdFile.new_paragraph(f"**Description:** {cve_description}")
            mdFile.new_paragraph(f"**Severity:** {cve_severity}")
        else:
            mdFile.new_line()
            mdFile.new_header(level=1, title=f"No details found for {cve_id}")
    else:
        mdFile.new_line()
        mdFile.new_header(level=1, title=f"Error fetching details for {cve_id}: {response.status_code}")

# Create the markdown file
mdFile.create_md_file()