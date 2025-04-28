import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Convert 'Timestamp' and extract 'Year'
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Helper to generate colors from colormaps
def get_colors(cmap, count):
    return [cmap(i) for i in np.linspace(0, 1, count)]

# Pie Chart 1: Attack Type
if 'Attack Type' in df.columns:
    data = df['Attack Type'].value_counts()
    plt.figure(figsize=(6, 6))
    data.plot.pie(autopct='%1.1f%%', startangle=140, colors=get_colors(plt.cm.Set2, len(data)))
    plt.title('Attack Type Distribution')
    plt.ylabel('')
    plt.show()

# Pie Chart 2: Attack Severity
if 'Attack Severity' in df.columns:
    data = df['Attack Severity'].value_counts()
    plt.figure(figsize=(6, 6))
    data.plot.pie(autopct='%1.1f%%', startangle=140, colors=get_colors(plt.cm.Reds, len(data)))
    plt.title('Attack Severity Distribution')
    plt.ylabel('')
    plt.show()

# Pie Chart 3: Response Action
if 'Response Action' in df.columns:
    data = df['Response Action'].value_counts()
    plt.figure(figsize=(6, 6))
    data.plot.pie(autopct='%1.1f%%', startangle=140, colors=get_colors(plt.cm.Blues, len(data)))
    plt.title('Response Action Distribution')
    plt.ylabel('')
    plt.show()

# Pie Chart 4: Data Exfiltrated
if 'Data Exfiltrated' in df.columns:
    data = df['Data Exfiltrated'].value_counts()
    plt.figure(figsize=(6, 6))
    data.plot.pie(autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
    plt.title('Data Exfiltrated (True/False)')
    plt.ylabel('')
    plt.show()

# Pie Chart 5: Top 5 Years with Most Attacks
if 'Year' in df.columns:
    data = df['Year'].value_counts().nlargest(5)
    plt.figure(figsize=(6, 6))
    data.plot.pie(autopct='%1.1f%%', startangle=140, colors=get_colors(plt.cm.Set3, len(data)))
    plt.title('Top 5 Years with Most Attacks')
    plt.ylabel('')
    plt.show()
