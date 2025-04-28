import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()

# Convert Timestamp to datetime and extract hour
if 'Timestamp' in df.columns:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    df['Hour'] = df['Timestamp'].dt.hour

# Plot Top 5 hours with most attacks
if 'Hour' in df.columns:
    top_hours = df['Hour'].value_counts().nlargest(5).sort_index()
    plt.figure(figsize=(8, 4))
    sns.barplot(x=top_hours.index, y=top_hours.values, palette='coolwarm')
    plt.title("Top 5 Hours When Attacks Occurred")
    plt.xlabel("Hour of Day")
    plt.ylabel("Attack Count")
    plt.tight_layout()
    plt.show()
