import pandas as pd

# Path to the CSV file
file_path = r"D:\MY_REPO\data\auto_trip_ford_8h\auto_trip.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Convert the timestamp column to datetime if it's not already
# Assuming the timestamp column is named 'time'
df['time'] = pd.to_datetime(df['time'])

# Set the timestamp column as the index
df.set_index('time', inplace=True)

# Resample the data to 1-second intervals and calculate the mean
resampled_df = df.resample('1S').mean()

# Path to save the resampled CSV file on the desktop
output_file_path = r"C:\Users\S\Desktop\resampled_auto_trip.csv"

# Save the resampled DataFrame to a CSV file
resampled_df.to_csv(output_file_path)

print(f"Resampled data saved to {output_file_path}")
