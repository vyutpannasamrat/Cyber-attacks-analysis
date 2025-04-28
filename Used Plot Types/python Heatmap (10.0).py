import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Parse timestamp
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Set seaborn style
sns.set(style="whitegrid")

# Heatmap 1: Attack Type vs Attack Severity
if 'Attack Type' in df.columns and 'Attack Severity' in df.columns:
    pivot1 = df.pivot_table(index='Attack Type', columns='Attack Severity', aggfunc='size', fill_value=0)
    plt.figure(figsize=(8, 6))
    sns.heatmap(pivot1, annot=True, cmap="YlGnBu")
    plt.title("Heatmap: Attack Type vs Attack Severity")
    plt.tight_layout()
    plt.show()

# Heatmap 2: Response Action vs Attack Type
if 'Response Action' in df.columns and 'Attack Type' in df.columns:
    pivot2 = df.pivot_table(index='Response Action', columns='Attack Type', aggfunc='size', fill_value=0)
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot2, annot=True, cmap="Oranges")
    plt.title("Heatmap: Response Action vs Attack Type")
    plt.tight_layout()
    plt.show()

# Heatmap 3: Attack Type vs Data Exfiltrated
if 'Attack Type' in df.columns and 'Data Exfiltrated' in df.columns:
    pivot3 = df.pivot_table(index='Attack Type', columns='Data Exfiltrated', aggfunc='size', fill_value=0)
    plt.figure(figsize=(7, 5))
    sns.heatmap(pivot3, annot=True, cmap="coolwarm")
    plt.title("Heatmap: Attack Type vs Data Exfiltrated")
    plt.tight_layout()
    plt.show()

# Heatmap 4: Year vs Attack Severity
if 'Year' in df.columns and 'Attack Severity' in df.columns:
    pivot4 = df.pivot_table(index='Year', columns='Attack Severity', aggfunc='size', fill_value=0)
    plt.figure(figsize=(8, 5))
    sns.heatmap(pivot4, annot=True, cmap="PuRd")
    plt.title("Heatmap: Year vs Attack Severity")
    plt.tight_layout()
    plt.show()

# Heatmap 5: Year vs Response Action
if 'Year' in df.columns and 'Response Action' in df.columns:
    pivot5 = df.pivot_table(index='Year', columns='Response Action', aggfunc='size', fill_value=0)
    plt.figure(figsize=(10, 5))
    sns.heatmap(pivot5, annot=True, cmap="BuPu")
    plt.title("Heatmap: Year vs Response Action")
    plt.tight_layout()
    plt.show()
