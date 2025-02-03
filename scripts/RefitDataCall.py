import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace 'refit_dataset.csv' with the path to your dataset file
df = pd.read_csv("/home/teeker/Data/ets-refit/CLEAN_REFIT_081116/CLEAN_House1.csv")
print(df.head())

print(df.info())
print(df.describe())


# Assuming the dataset has columns 'timestamp' and 'power'
# df['DateTime'] = pd.to_datetime(df['DateTime'])
plt.figure(figsize=(10, 6))
sns.lineplot(x='Unix', y='Aggregate', data=df)
plt.xlabel('Time')
plt.ylabel('Power Consumption (W)')
plt.title('Power Consumption Over Time')
plt.xticks(rotation=45)
plt.show()
