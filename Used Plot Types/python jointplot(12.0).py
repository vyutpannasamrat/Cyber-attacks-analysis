import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and prepare the data
df = pd.read_csv("ai_ml_cybersecurity_dataset.csv")
df.columns = df.columns.str.strip()
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df['Year'] = df['Timestamp'].dt.year

# Group by year to count incidents
yearly_counts = df['Year'].value_counts().sort_index()
df_years = pd.DataFrame({'Year': yearly_counts.index, 'Attack Count': yearly_counts.values})

# Joint plot with KDE and histograms
sns.set(style="white", font_scale=1.1)
g = sns.jointplot(data=df_years, x='Year', y='Attack Count', kind='kde', fill=True, cmap="Blues", height=8)

# Adjust plot titles and spacing
g.ax_joint.set_title("Joint Distribution of Attacks Over the Years", fontsize=14, pad=40)
plt.tight_layout()
plt.show()
