import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('C:\Python\premier-player-23-24.csv')

# Preview
print("🔍 First 5 rows:\n", df.head())

# Clean numeric columns
numeric_cols = ['Age', 'MP', 'Starts', 'Min', '90s', 'Gls', 'Ast', 'G+A', 'G-PK',
                'PK', 'PKatt', 'CrdY', 'CrdR', 'xG', 'npxG', 'xAG', 'npxG+xAG',
                'PrgC', 'PrgP', 'PrgR']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop nulls from key stats
df = df.dropna(subset=['Gls', 'Ast', 'xG', 'xAG'])

# --- Top Goal Scorers ---
top_goals = df.sort_values('Gls', ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x='Gls', y='Player', data=top_goals, palette='Reds_r')
plt.title('Top 10 Goal Scorers (Premier League 2023/24)')
plt.xlabel('Goals')
plt.tight_layout()
plt.show()

# --- Top Assisters ---
top_assists = df.sort_values('Ast', ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x='Ast', y='Player', data=top_assists, palette='Blues_r')
plt.title('Top 10 Assist Providers')
plt.xlabel('Assists')
plt.tight_layout()
plt.show()

# --- xG vs Goals Scatter ---
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='xG', y='Gls', hue='Pos')
plt.title('Expected Goals (xG) vs Actual Goals')
plt.xlabel('xG')
plt.ylabel('Goals')
plt.tight_layout()
plt.show()

# --- Progressive Carries by Player ---
top_carries = df.sort_values('PrgC', ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x='PrgC', y='Player', data=top_carries, palette='Greens_r')
plt.title('Top 10 Players by Progressive Carries')
plt.xlabel('Progressive Carries')
plt.tight_layout()
plt.show()

# --- Position Distribution ---
plt.figure(figsize=(8,6))
sns.countplot(data=df, x='Pos', palette='pastel')
plt.title('Player Count by Position')
plt.xlabel('Position')
plt.tight_layout()
plt.show()

# --- Age Distribution ---
plt.figure(figsize=(10,5))
sns.histplot(df['Age'], kde=True, bins=15, color='purple')
plt.title('Age Distribution of Players')
plt.xlabel('Age')
plt.tight_layout()
plt.show()
