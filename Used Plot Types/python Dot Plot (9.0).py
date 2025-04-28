import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Count values for each column and make a dot plot
def dot_plot(column_name, title):
    counts = df[column_name].value_counts().sort_values()
    plt.figure(figsize=(8, 4))
    plt.plot(counts.values, counts.index, 'o', markersize=10)
    plt.title(title)
    plt.xlabel('Count')
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# Dot Plot 1: Attack Type
if 'Attack Type' in df.columns:
    dot_plot('Attack Type', 'Dot Plot of Attack Type')

# Dot Plot 2: Attack Severity
if 'Attack Severity' in df.columns:
    dot_plot('Attack Severity', 'Dot Plot of Attack Severity')

# Dot Plot 3: Response Action
if 'Response Action' in df.columns:
    dot_plot('Response Action', 'Dot Plot of Response Action')

# Dot Plot 4: Data Exfiltrated
if 'Data Exfiltrated' in df.columns:
    dot_plot('Data Exfiltrated', 'Dot Plot of Data Exfiltrated')

# Dot Plot 5: Top 5 Years with Most Attacks
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year
top_years = df['Year'].value_counts().nlargest(5).sort_values()
plt.figure(figsize=(8, 4))
plt.plot(top_years.values, top_years.index, 'o', markersize=10, color='purple')
plt.title('Dot Plot of Top 5 Years with Most Attacks')
plt.xlabel('Count')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
