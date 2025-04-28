import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean the dataset
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Convert timestamp to datetime and extract year
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Set style
sns.set(style="whitegrid")

# 1. Line Plot: Attack Type over Years
if 'Attack Type' in df.columns:
    attack_trend = df.groupby(['Year', 'Attack Type']).size().unstack(fill_value=0)
    attack_trend.plot(figsize=(10, 5), marker='o')
    plt.title("Yearly Trend of Attack Types")
    plt.xlabel("Year")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 2. Line Plot: Severity over Years
if 'Attack Severity' in df.columns:
    severity_trend = df.groupby(['Year', 'Attack Severity']).size().unstack(fill_value=0)
    severity_trend.plot(figsize=(10, 5), marker='o')
    plt.title("Yearly Trend of Attack Severity")
    plt.xlabel("Year")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 3. Line Plot: Response Action over Years
if 'Response Action' in df.columns:
    response_trend = df.groupby(['Year', 'Response Action']).size().unstack(fill_value=0)
    response_trend.plot(figsize=(10, 5), marker='o')
    plt.title("Yearly Trend of Response Actions")
    plt.xlabel("Year")
    plt.ylabel("Number of Responses")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 4. Line Plot: Total Incidents per Year
incident_trend = df.groupby('Year').size()
incident_trend.plot(figsize=(10, 5), marker='o', color='purple')
plt.title("Total Cybersecurity Incidents per Year")
plt.xlabel("Year")
plt.ylabel("Total Incidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
