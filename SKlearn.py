import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('abc_manufacturing_data.csv')

# Explore the data
print(df.head())
print(df.info())
print(df.describe())

# Visualize the data
plt.figure(figsize=(12, 8))
sns.pairplot(df)
plt.show()

# Compute the correlation matrix
corr_matrix = df.corr()
print(corr_matrix)



# Select the features
X = df[['feature1', 'feature2', 'feature3']]
y = df['target_variable']

