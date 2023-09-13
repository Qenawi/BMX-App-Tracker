import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Read the CSV data from a file
data = pd.read_csv('path/to/your/csv/file.csv', delimiter=';')

# Extract relevant columns
date_column = data['Date']
version_column = data['Version']
star_columns = data[['5 star', '4 star', '3 star', '2 star', '1 star']]

# Calculate the total star count for each row
star_columns['Total Stars'] = star_columns.sum(axis=1)

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(date_column, star_columns['Total Stars'], label='Total Stars', marker='o', linestyle='-')
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Total Stars')
plt.title('Total Stars Over Time')
plt.legend(loc='upper right')

# Show version numbers as annotations
for i, version in enumerate(version_column):
    plt.annotate(version, (date_column[i], star_columns['Total Stars'][i]))

plt.tight_layout()
plt.savefig('plots/generated_plot.png')  # Save the plot to a fil
