#!/usr/bin/python3

# 
# Usage: python3 search.py <vendor regex> <product regex> <version regex>"
#
# Return codes :
#    0: cpe found and is unique.
#    1: missing parameters.
#    2: more than one vendor identified.
#    3: no vendor identified.
#    4: more than one cpe found.
#    5: no matching cpe found.
  

import requests
import sys
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# ANSII colors: to print in console
RED = "\033[1;31m"
YELLOW = "\033[33m"
RESET = "\033[0m"


if len(sys.argv) != 4 or sys.argv[1] == "-h":
    print(f"Usage: {YELLOW}search.py <vendor regex> <product regex> <version regex>{RESET}")
    print(f"Examples:")
    print(f'\t./search_cpe.py "^telnetd" telnetd "0.17.2"')
    print(f'\t./search_cpe.py "openbsd" openssh 4.7p1')
    sys.exit(1)
vendor=sys.argv[1]
product=sys.argv[2]
version=sys.argv[3]

print (f"Vendor: {YELLOW}" + vendor + f"{RESET}\tProduct: " + f"{YELLOW}" + product + f"{RESET}\tVersion:" + f"{YELLOW}" + version + f"{RESET}")

# Disable:  InsecureRequestWarning: Unverified HTTPS request is being made to host 'localhost'
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

payload={}
headers = {
    'X-Api-Key': 'f06b8e71-9eda-46e5-9dd9-1b73d18440ce'
}

# --------------------------------------------------------
# Browse all the known vendors
# --------------------------------------------------------
url = "https://localhost:8443/api/browse"
print (f"CVE-search API call: {YELLOW}" + url + f"{RESET}" )

response = requests.get(url, headers=headers, data=payload, verify=False)
json = response.json()
vendor_values = json.get('vendor', '')

# Regex for identifying the vendor
regex_vendor = r'.*' + vendor + '.*'

vendor_matches = []
ctr_values=0

for vendor_value in vendor_values:
    if re.match(regex_vendor, vendor_value):
        ctr_values += 1
        vendor_matches.append(vendor_value)

if ctr_values > 1:  # More than one vendor identified: parameter "vendor Regex" not enough selective
    print (f"Nb vendors:{RED}", ctr_values)
    print (f"\tUse a more restrictive REGEX to identify the vendor")
    if ctr_values <20:  # If < 20, still displayed (not too many lines)
        print (f"{RESET}Identified vendors:")
        print ("\t",vendor_matches)
    sys.exit(2)

if vendor_matches:
    vendor=", ".join(vendor_matches)
    print(f"Vendor matching: {YELLOW}", vendor, f"{RESET}")
else:
    print(f"{RED}No vendor values match the regex:", regex_vendor)
    sys.exit(3)


# --------------------------------------------------------
# Browse all the products for the identified vendor
# --------------------------------------------------------
url = "https://localhost:8443/api/search/" + vendor + "/" + product
print (f"CVE-search API call: {YELLOW}", url)

response = requests.get(url, headers=headers, data=payload, verify=False)
json = response.json()
vulnerable_products = json.get('vulnerable_product', '')

# Regex for identifying the cpe string
regex_cpe = r'.*' + product + '.*' + version + '.*'

cpe_matches = []

for result in json.get('results', []):
    vulnerable_products = result.get('vulnerable_product', [])
    for vulnerable_product in vulnerable_products:
        # Does the regex match the attribute vulnerable_product
        if re.match(regex_cpe, vulnerable_product):
            cpe_matches.append(vulnerable_product)

# Remove duplicate values for cpe
unique_cpe = sorted(set(cpe_matches))

if cpe_matches:
    print(f"{RESET}CPE matching:{YELLOW}", unique_cpe)
    ctr_cpe = len(unique_cpe)
    if ctr_cpe>1:
        print (f"More than one cpe:{RED}", ctr_cpe, "identified")
        print (f"\tUse a more restrictive REGEX to identify the CPE: try adding more characters to the product and/or the version regex")
        sys.exit(4)
else:
    print(f"{RED}No vulnerable_product values match the regex:", regex_cpe)
    sys.exit(5)

sys.exit(0)    