import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Convert timestamp and extract year
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Set seaborn style
sns.set(style="whitegrid")

# Function to plot boxplot from value_counts
def plot_box_from_counts(series, title):
    counts = series.value_counts().values  # just the counts as a numeric array
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=counts)
    plt.title(title)
    plt.xlabel("Count")
    plt.show()

# Box Plot 1: Attack Type Counts
if 'Attack Type' in df.columns:
    plot_box_from_counts(df['Attack Type'], 'Box Plot of Attack Type Frequencies')

# Box Plot 2: Attack Severity Counts
if 'Attack Severity' in df.columns:
    plot_box_from_counts(df['Attack Severity'], 'Box Plot of Attack Severity Frequencies')

# Box Plot 3: Response Action Counts
if 'Response Action' in df.columns:
    plot_box_from_counts(df['Response Action'], 'Box Plot of Response Action Frequencies')

# Box Plot 4: Data Exfiltrated Counts
if 'Data Exfiltrated' in df.columns:
    plot_box_from_counts(df['Data Exfiltrated'], 'Box Plot of Data Exfiltrated Frequencies')

# Box Plot 5: Number of Attacks per Year
if 'Year' in df.columns:
    year_counts = df['Year'].value_counts().values
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=year_counts)
    plt.title('Box Plot of Attack Counts per Year')
    plt.xlabel("Count")
    plt.show()
