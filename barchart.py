import matplotlib.pyplot as plt

# Data
countries = [
    'India', 'China', 'United States', 'Indonesia', 'Pakistan',
    'Nigeria', 'Brazil', 'Bangladesh', 'Russia', 'Ethiopia'
]
populations = [
    1463865525, 1416096094, 347275807, 285721236, 255219554,
    237527782, 212812405, 175686899, 143997393, 135472051
]

# Convert population to millions for readability
populations_millions = [pop / 1e6 for pop in populations]

# Plot
plt.figure(figsize=(12, 8))
bars = plt.barh(countries, populations_millions, color='skyblue')
plt.xlabel('Population (in millions)')
plt.title('Top 10 Most Populous Countries in 2025')
plt.gca().invert_yaxis()  # Highest population on top

# Add labels to bars
for bar in bars:
    width = bar.get_width()
    plt.text(width + 5, bar.get_y() + bar.get_height()/2,
             f'{width:.1f}M', va='center')

plt.tight_layout()
plt.show()
