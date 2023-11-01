import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('IDCJAC0009_086071_1800_Data.csv',
                 names=["Product_ID", "Station_No", "Year", "Day", "Month", "Year2", "Rainfall", "Continuous_Days", "Quality_Indicator"],
                 skiprows=1)  # Assumes the first row is a header

# Drop the duplicated 'Year2' column
df = df.drop(columns=['Year2'])

# Convert 'Rainfall' to numeric, setting errors='coerce' to handle invalid data by setting them as NaN
df['Rainfall'] = pd.to_numeric(df['Rainfall'], errors='coerce')

# Calculate monthly statistics
monthly_stats = df.groupby(['Year', 'Month']).Rainfall.agg(['sum', 'mean', 'std'])

# Calculate annual statistics
annual_stats = df.groupby(['Year']).Rainfall.agg(['sum', 'mean', 'std'])

# Print monthly and annual statistics
print("Monthly Rainfall Statistics")
print(monthly_stats)

print("\nAnnual Rainfall Statistics")
print(annual_stats)

# Optional: Save the statistics to CSV
monthly_stats.to_csv('monthly_rainfall_statistics.csv')
annual_stats.to_csv('annual_rainfall_statistics.csv')

