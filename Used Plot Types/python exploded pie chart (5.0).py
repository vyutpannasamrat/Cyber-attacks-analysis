import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Convert timestamp and extract year
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Helper function to create pie chart with lowest value popped out
def plot_exploded_pie(data, title, cmap):
    explode = [0.1 if v == data.min() else 0 for v in data]
    colors = cmap(np.linspace(0.3, 0.9, len(data)))
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140,
            colors=colors, explode=explode)
    plt.title(title)
    plt.ylabel('')
    plt.show()

# Pie Chart 1: Attack Type
if 'Attack Type' in df.columns:
    data = df['Attack Type'].value_counts()
    plot_exploded_pie(data, 'Attack Type Distribution (Lowest Popped)', plt.cm.Set2)

# Pie Chart 2: Attack Severity
if 'Attack Severity' in df.columns:
    data = df['Attack Severity'].value_counts()
    plot_exploded_pie(data, 'Attack Severity Distribution (Lowest Popped)', plt.cm.Reds)

# Pie Chart 3: Response Action
if 'Response Action' in df.columns:
    data = df['Response Action'].value_counts()
    plot_exploded_pie(data, 'Response Action Distribution (Lowest Popped)', plt.cm.Blues)

# Pie Chart 4: Data Exfiltrated
if 'Data Exfiltrated' in df.columns:
    data = df['Data Exfiltrated'].value_counts()
    plot_exploded_pie(data, 'Data Exfiltrated (Lowest Popped)', plt.cm.Paired)

# Pie Chart 5: Top 5 Years with Most Attacks
if 'Year' in df.columns:
    data = df['Year'].value_counts().nlargest(5)
    plot_exploded_pie(data, 'Top 5 Years with Most Attacks (Lowest Popped)', plt.cm.Set3)
