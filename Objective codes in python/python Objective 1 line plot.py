import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Convert timestamp to datetime and extract year
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Group by year and attack type
trend_data = df.groupby(['Year', 'Attack Type']).size().reset_index(name='Count')

# Plot line chart: Attack trends over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=trend_data, x='Year', y='Count', hue='Attack Type', marker='o')
plt.title('Cyberattack Trends Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Attack Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
