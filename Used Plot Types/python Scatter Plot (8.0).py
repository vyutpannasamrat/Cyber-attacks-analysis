import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Convert timestamp to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Encode categorical data
df['Attack Type Code'] = df['Attack Type'].astype('category').cat.codes
df['Severity Code'] = df['Attack Severity'].astype('category').cat.codes
df['Response Code'] = df['Response Action'].astype('category').cat.codes
df['Exfil Code'] = df['Data Exfiltrated'].astype('category').cat.codes

# Helper function to add jitter
def jitter(arr, scale=0.3):
    return arr + np.random.uniform(-scale, scale, size=arr.shape)

# Scatter Plot 1: Attack Type vs Year
plt.figure(figsize=(6, 4))
plt.scatter(jitter(df['Year'].dropna()), jitter(df['Attack Type Code'].dropna()), alpha=0.5)
plt.title("Attack Type vs Year (with Jitter)")
plt.xlabel("Year")
plt.ylabel("Attack Type Code")
plt.tight_layout()
plt.show()

# Scatter Plot 2: Attack Severity vs Year
plt.figure(figsize=(6, 4))
plt.scatter(jitter(df['Year'].dropna()), jitter(df['Severity Code'].dropna()), alpha=0.5, color='orange')
plt.title("Attack Severity vs Year (with Jitter)")
plt.xlabel("Year")
plt.ylabel("Severity Code")
plt.tight_layout()
plt.show()

# Scatter Plot 3: Response Action vs Year
plt.figure(figsize=(6, 4))
plt.scatter(jitter(df['Year'].dropna()), jitter(df['Response Code'].dropna()), alpha=0.5, color='green')
plt.title("Response Action vs Year (with Jitter)")
plt.xlabel("Year")
plt.ylabel("Response Code")
plt.tight_layout()
plt.show()

# Scatter Plot 4: Data Exfiltrated vs Year
plt.figure(figsize=(6, 4))
plt.scatter(jitter(df['Year'].dropna()), jitter(df['Exfil Code'].dropna()), alpha=0.5, color='purple')
plt.title("Data Exfiltrated vs Year (with Jitter)")
plt.xlabel("Year")
plt.ylabel("Data Exfiltrated Code")
plt.tight_layout()
plt.show()

# Scatter Plot 5: Attack Type vs Severity
plt.figure(figsize=(6, 4))
plt.scatter(jitter(df['Attack Type Code'].dropna()), jitter(df['Severity Code'].dropna()), alpha=0.5, color='red')
plt.title("Attack Type vs Attack Severity (with Jitter)")
plt.xlabel("Attack Type Code")
plt.ylabel("Attack Severity Code")
plt.tight_layout()
plt.show()
