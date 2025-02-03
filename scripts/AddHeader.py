import pandas as pd

# Load the CSV file without header
df = pd.read_csv('C:\Data\REFITPowerData111215\House1.csv', header=None)

# Define the header
# DateTime (YYYY-MM-DD HH:mm:ss), UNIX TIMESTAMP (UCT), Aggregate, Appliance1, Appliance2, Appliance3, ... , Appliance9
column_names = ['DateTime', 'timestamp', 'Aggregate', 'Appliance1', 'Appliance2', 'Appliance3', 'Appliance4', 'Appliance5', 'Appliance6', 'Appliance7', 'Appliance8']

# Assign the header to the DataFrame
df.columns = column_names

# Save the updated DataFrame to a new CSV file
df.to_csv('C:\Data\REFITPowerData111215\House1_AddHead.csv', index=False)

print(df.head())
