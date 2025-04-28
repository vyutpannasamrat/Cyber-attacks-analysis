import pandas as pd
import matplotlib.pyplot as plt

# Load and clean the dataset
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Group by Year and Attack Type
attack_year = df.groupby(['Year', 'Attack Type']).size().unstack(fill_value=0)

# Plot stacked bar chart
attack_year.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set3')
plt.title('Stacked Bar Chart of Attack Types per Year')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=45)
plt.legend(title='Attack Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
