from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
print(df.head())

# Total Goals Scored
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df['Total Goals'].head())

sns.set_style('whitegrid')
sns.set_context('poster', font_scale = 0.8)

f, ax = plt.subplots(figsize = (12, 7))
ax = sns.barplot(x = "Year",
                 y = "Total Goals",
                 data = df)
ax.set_title("Average Number of Goals Scored In Word Cup Matches By Year")   




df_goals = pd.read_csv('goals.csv')
print(df_goals.head())

sns.set_style('whitegrid')
sns.set_context('notebook', font_scale = 1.25)
f, ax2 = plt.subplots(figsize = (12, 7))

ax2 = sns.boxplot(x = "year",
                  y = "goals",
                  data = df_goals,
                  palette = "Spectral")
ax2.set_title("Goals Visualization")

plt.show()
                 




