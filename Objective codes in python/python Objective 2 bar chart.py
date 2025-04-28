import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean the dataset
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Count frequency of each combination of Attack Type and Severity
severity_data = df.groupby(['Attack Type', 'Attack Severity']).size().reset_index(name='Count')

# Sort by severity level (optional: you may define custom sort order)
severity_order = ['Low', 'Medium', 'High', 'Critical']  # adjust if needed
if set(severity_order).issubset(set(severity_data['Attack Severity'].unique())):
    severity_data['Attack Severity'] = pd.Categorical(severity_data['Attack Severity'], categories=severity_order, ordered=True)
    severity_data = severity_data.sort_values(by=['Attack Severity', 'Count'], ascending=[False, False])

# Plot a grouped bar chart
plt.figure(figsize=(12, 6))
sns.barplot(data=severity_data, x='Attack Type', y='Count', hue='Attack Severity', palette='Reds')
plt.title('Attack Severity Levels by Attack Type')
plt.xlabel('Attack Type')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Attack Severity', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
