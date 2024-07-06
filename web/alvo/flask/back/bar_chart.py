#!/usr/bin/python3

import re
from collections import Counter
import sys
import os
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print("Usage: python generate_report.py <markdown file>")
    sys.exit(1)

file_path = sys.argv[1]

service_names = []
with open(file_path, 'r') as file:
    for line in file:
        match = re.search(r'cpe:2.3:a:(.*?):(.*?):', line)
        if match:
            service_names.append(match.group(2))

service_counts = Counter(service_names)

sorted_services = sorted(service_counts.items(), key=lambda x: x[1], reverse=True)
services, vulnerabilities = zip(*sorted_services)

# Plotting
plt.figure(figsize=(10, 8))
plt.barh(services, vulnerabilities, color='skyblue')
plt.xlabel('Number of Vulnerabilities')
plt.ylabel('Services')
plt.title('Number of Vulnerabilities by Service')
plt.gca().invert_yaxis() 

# Save the plot to file using full path
base_path = os.path.dirname(__file__)
plt.savefig(base_path + '/alvo_bar_chart.png')