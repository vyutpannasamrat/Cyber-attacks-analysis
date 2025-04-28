import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean the dataset
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Create a crosstab between Attack Type and Attack Severity
heatmap_data = pd.crosstab(df['Attack Type'], df['Attack Severity'])

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Heatmap of Attack Type vs. Attack Severity')
plt.xlabel('Attack Severity')
plt.ylabel('Attack Type')
plt.tight_layout()
plt.show()
