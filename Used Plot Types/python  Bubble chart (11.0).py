import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and prepare data
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Group by Attack Type and Severity to get frequency
bubble_data = df.groupby(['Attack Type', 'Attack Severity']).size().reset_index(name='Count')

# Plot Bubble Chart
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=bubble_data,
    x='Attack Type',
    y='Attack Severity',
    size='Count',
    legend=False,
    sizes=(100, 1500),
    alpha=0.6
)
plt.title('Bubble Chart: Attack Type vs Severity (Bubble = Frequency)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
