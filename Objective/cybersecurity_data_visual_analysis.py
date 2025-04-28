import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Convert Timestamp and extract Year
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Objective 1: Analyze the distribution of attack types
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Attack Type', hue='Attack Type',
              order=df['Attack Type'].value_counts().index,
              palette='Set2', legend=False)
plt.title("Distribution of Attack Types")
plt.xlabel("Attack Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Objective 2: Identify top 5 years with most attacks using a pie chart
top5_years = df['Year'].value_counts().nlargest(5)
plt.figure(figsize=(6, 6))
explode = [0.1 if i == top5_years.idxmin() else 0 for i in top5_years.index]
plt.pie(top5_years, labels=top5_years.index, autopct='%1.1f%%',
        startangle=140, explode=explode, colors=plt.cm.Set3.colors)
plt.title("Top 5 Years with Most Attacks")
plt.tight_layout()
plt.show()

# Objective 3: Compare attack severity using violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(data=df, x='Attack Severity', hue='Attack Severity',
               inner='box', palette='Set3', legend=False)
plt.title("Attack Severity Distribution")
plt.xlabel("Attack Severity")
plt.tight_layout()
plt.show()

# Objective 4: Relationship between attack severity and response action using heatmap
pivot_table = pd.crosstab(df['Attack Severity'], df['Response Action'])
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt='d')
plt.title("Heatmap: Attack Severity vs Response Action")
plt.xlabel("Response Action")
plt.ylabel("Attack Severity")
plt.tight_layout()
plt.show()

# Objective 5: Show Data Exfiltrated proportions using pie chart
data_exfiltrated_counts = df['Data Exfiltrated'].value_counts()
plt.figure(figsize=(6, 6))
explode = [0.1 if data_exfiltrated_counts[i] == data_exfiltrated_counts.min() else 0
           for i in data_exfiltrated_counts.index]
plt.pie(data_exfiltrated_counts, labels=data_exfiltrated_counts.index,
        autopct='%1.1f%%', startangle=140, explode=explode,
        colors=['#ff9999', '#66b3ff'])
plt.title("Data Exfiltrated (True/False)")
plt.tight_layout()
plt.show()
