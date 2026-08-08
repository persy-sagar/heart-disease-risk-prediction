import pandas as pd

df = pd.read_csv('data/heart.csv')

# Basic info
print(df.shape)
print(df.info())
print(df.isnull().sum())          # check missing values
print(df['HeartDisease'].value_counts())   # check class balance (0 = no disease, 1 = disease)

# Correlation with target (numeric columns only)
print(df.corr(numeric_only=True)['HeartDisease'].sort_values(ascending=False))