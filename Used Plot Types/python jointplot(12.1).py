import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and prepare data
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Count attacks per year
year_counts = df['Year'].value_counts().reset_index()
year_counts.columns = ['Year', 'Attack Count']

# Plot Joint Plot
sns.jointplot(
    data=year_counts,
    x='Year',
    y='Attack Count',
    kind='scatter',
    marginal_kws=dict(bins=10, fill=True),
    color='purple'
)
plt.suptitle("Joint Plot: Year vs Attack Count", y=1.02)
plt.show()
