import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load your cleaned data
df = pd.read_csv('/Users/zainab/Desktop/jarir_updated.csv')

# Visualizations
# Brand Distribution

plt.figure(figsize=(10, 6))
sns.countplot(y=df['Brand'], order=df['Brand'].value_counts().index)
plt.title('Brand Distribution')
plt.xlabel('Count')
plt.ylabel('Brand')
plt.show()