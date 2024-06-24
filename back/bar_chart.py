#!/usr/bin/python3

import matplotlib.pyplot as plt
import re
from collections import Counter

service_names = []
with open('report.md', 'r') as file:
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
plt.savefig('alvo_bar_chart.png')