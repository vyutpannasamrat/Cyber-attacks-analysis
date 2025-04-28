import pandas as pd
import matplotlib.pyplot as plt

# Load and clean the dataset
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Convert Timestamp and extract year
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Get counts of attacks per year
year_counts = df['Year'].value_counts().sort_index()

# Plot pie chart
plt.figure(figsize=(7, 7))
explode = [0.1 if val == year_counts.min() else 0 for val in year_counts]  # pop out the year with least attacks
plt.pie(year_counts, labels=year_counts.index, autopct='%1.1f%%', startangle=140, explode=explode, colors=plt.cm.Set3.colors)
plt.title('Proportion of Cyber Attacks by Year')
plt.axis('equal')  # Equal aspect ratio ensures the pie is circular
plt.tight_layout()
plt.show()
