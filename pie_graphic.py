#!/usr/bin/python3

import re
import matplotlib.pyplot as plt

# Function to categorize CVSS scores into severity levels
def categorize_cvss(score):
    if score >= 0 and score < 4:
        return 'Low'
    elif score >= 4 and score < 7:
        return 'Medium'
    elif score >= 7 and score < 9:
        return 'High'
    elif score >= 9 and score <= 10:
        return 'Critical'
    else:
        return 'Unknown'

# Read the Markdown file
file_path = 'report.md'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Regular expression to find all instances of "cvss: <number>"
pattern = r'CVSS:\s*(\d+(\.\d+)?)'
matches = re.findall(pattern, content)

print("Matches found:", matches)

cvss_scores = [float(match[0]) for match in matches]

print("CVSS scores extracted:", cvss_scores)

categories = ['Low', 'Medium', 'High', 'Critical']
category_counts = {category: 0 for category in categories}

for score in cvss_scores:
    category = categorize_cvss(score)
    category_counts[category] += 1

# Debugging: Print category counts to verify
print("Category counts:", category_counts)

# Prepare data for pie chart
labels = [category for category in categories if category_counts[category] > 0]
sizes = [category_counts[category] for category in labels]

# Define colors: red for Critical, shades of blue and grey for others
colors = ['#ff6666', '#66b3ff', '#99ff99', '#666666']

# Calculate explode based on the number of categories
explode = [0.1 if category == 'Low' else 0 for category in labels]

# Debugging: Print data for pie chart
print("Labels:", labels)
print("Sizes:", sizes)
print("Explode:", explode)

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('CVSS Severity Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Save the plot to a file (e.g., PNG)
plt.savefig('alvo_pie_chart.png')
