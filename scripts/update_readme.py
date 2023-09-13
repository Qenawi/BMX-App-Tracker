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

# Update the README with insights
with open('README.md', 'r') as readme_file:
    readme_content = readme_file.read()

readme_content = readme_content.replace('{{HIGHEST_STARS}}', str(highest_stars))
readme_content = readme_content.replace('{{LOWEST_STARS}}', str(lowest_stars))

with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content)
