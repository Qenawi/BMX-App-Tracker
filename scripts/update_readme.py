import pandas as pd

# Read the CSV data and calculate insights
def calculate_insights(data):
    highest_stars = data[['5 star', '4 star', '3 star', '2 star', '1 star']].max().max()
    lowest_stars = data[['5 star', '4 star', '3 star', '2 star', '1 star']].min().min()
    
    highest_row = data.loc[data[['5 star', '4 star', '3 star', '2 star', '1 star']].values == highest_stars]
    lowest_row = data.loc[data[['5 star', '4 star', '3 star', '2 star', '1 star']].values == lowest_stars]
    
    highest_version = highest_row['Version'].values[0]
    lowest_version = lowest_row['Version'].values[0]
    
    highest_date = highest_row['Date'].values[0]
    lowest_date = lowest_row['Date'].values[0]

    return highest_stars, lowest_stars, highest_version, lowest_version, highest_date, lowest_date

# Read the CSV file
data = pd.read_csv('data/data.csv', delimiter=';')

# Calculate insights
highest_stars, lowest_stars, highest_version, lowest_version, highest_date, lowest_date = calculate_insights(data)

# Read the README template
with open('README_template.md', 'r') as template_file:
    template_content = template_file.read()

# Replace placeholders with actual values
template_content = template_content.replace('{{HIGHEST_STARS}}', str(highest_stars))
template_content = template_content.replace('{{LOWEST_STARS}}', str(lowest_stars))
template_content = template_content.replace('{{HIGHEST_VERSION}}', highest_version)
template_content = template_content.replace('{{LOWEST_VERSION}}', lowest_version)
template_content = template_content.replace('{{HIGHEST_DATE}}', highest_date)
template_content = template_content.replace('{{LOWEST_DATE}}', lowest_date)

# Write the updated content to the README
with open('README.md', 'w') as readme_file:
    readme_file.write(template_content)
