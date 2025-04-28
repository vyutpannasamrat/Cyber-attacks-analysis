import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Graph 1: Attack Type Count
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Attack Type', hue='Attack Type', palette='Set2', legend=False)
plt.title("Count of Cyber Incidents by Attack Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graph 2: Attack Severity Count
plt.figure(figsize=(7, 4))
sns.countplot(data=df, x='Attack Severity', hue='Attack Severity', palette='Reds', legend=False)
plt.title("Attack Severity Distribution")
plt.tight_layout()
plt.show()

# Graph 3: Response Action Count
plt.figure(figsize=(8, 4))
sns.countplot(data=df, x='Response Action', hue='Response Action', palette='Blues', legend=False)
plt.title("Types of Response Actions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graph 4: Number of Attacks per Year
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year
year_counts = df['Year'].value_counts().sort_index().reset_index()
year_counts.columns = ['Year', 'Attack Count']

plt.figure(figsize=(8, 4))
sns.barplot(data=year_counts, x='Year', y='Attack Count', palette='magma')
plt.title("Number of Cyber Attacks Per Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
