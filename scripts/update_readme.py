import pandas as pd

# Read the CSV data and calculate insights
def calculate_insights(data):
    highest_stars = data[['5 star', '4 star', '3 star', '2 star', '1 star']].max().max()
    lowest_stars = data[['5 star', '4 star', '3 star', '2 star', '1 star']].min().min()

    return highest_stars, lowest_stars

# Read the CSV file
data = pd.read_csv('data/data.csv', delimiter=';')

# Calculate insights
highest_stars, lowest_stars = calculate_insights(data)

# Extract version number and date
version = data['Version'].iloc[-1]
date = data['Date'].iloc[-1]

# Read the README template
with open('README_template.md', 'r') as template_file:
    template_content = template_file.read()

# Replace placeholders with actual values
template_content = template_content.replace('{{HIGHEST_STARS}}', str(highest_stars))
template_content = template_content.replace('{{LOWEST_STARS}}', str(lowest_stars))
template_content = template_content.replace('{{VERSION}}', version)
template_content = template_content.replace('{{DATE}}', date)

# Write the updated content to the README
with open('README.md', 'w') as readme_file:
    readme_file.write(template_content)
