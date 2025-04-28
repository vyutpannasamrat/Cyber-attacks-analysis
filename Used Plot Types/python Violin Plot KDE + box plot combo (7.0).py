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

# Function to plot violin plot from value_counts
def plot_violin_from_counts(series, title):
    counts = series.value_counts().values  # numeric count values
    plt.figure(figsize=(6, 4))
    sns.violinplot(x=counts, inner="box", linewidth=1.2)
    plt.title(title)
    plt.xlabel("Count")
    plt.tight_layout()
    plt.show()

# Violin Plot 1: Attack Type Counts
if 'Attack Type' in df.columns:
    plot_violin_from_counts(df['Attack Type'], 'Violin Plot of Attack Type Frequencies')

# Violin Plot 2: Attack Severity Counts
if 'Attack Severity' in df.columns:
    plot_violin_from_counts(df['Attack Severity'], 'Violin Plot of Attack Severity Frequencies')

# Violin Plot 3: Response Action Counts
if 'Response Action' in df.columns:
    plot_violin_from_counts(df['Response Action'], 'Violin Plot of Response Action Frequencies')

# Violin Plot 4: Data Exfiltrated Counts
if 'Data Exfiltrated' in df.columns:
    plot_violin_from_counts(df['Data Exfiltrated'], 'Violin Plot of Data Exfiltrated Frequencies')

# Violin Plot 5: Attack Frequency by Year
if 'Year' in df.columns:
    year_counts = df['Year'].value_counts().values
    plt.figure(figsize=(6, 4))
    sns.violinplot(x=year_counts, inner="box", linewidth=1.2)
    plt.title('Violin Plot of Attack Counts per Year')
    plt.xlabel("Count")
    plt.tight_layout()
    plt.show()
