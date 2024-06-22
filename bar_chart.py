#!/usr/bin/python3

import matplotlib.pyplot as plt
import re
from collections import Counter

# Step 1: Extract service names from the CPE strings in the markdown file
service_names = []
with open('report.md', 'r') as file:
    for line in file:
        match = re.search(r'cpe:2.3:a:(.*?):(.*?):', line)
        if match:
            service_names.append(match.group(2))  # Group 2 is the product name

# Step 2: Aggregate data
service_counts = Counter(service_names)

# Step 3: Sort services by the number of vulnerabilities
sorted_services = sorted(service_counts.items(), key=lambda x: x[1], reverse=True)
services, vulnerabilities = zip(*sorted_services)

# Plotting
plt.figure(figsize=(10, 8))
plt.barh(services, vulnerabilities, color='skyblue')
plt.xlabel('Number of Vulnerabilities')
plt.ylabel('Services')
plt.title('Number of Vulnerabilities by Service')
plt.gca().invert_yaxis()  # Invert y-axis to have the service with the most vulnerabilities on top
plt.tight_layout()
plt.savefig('alvo_bar_chart.png')