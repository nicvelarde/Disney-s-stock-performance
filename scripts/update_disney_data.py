import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("isaaclopgu/the-walt-disney-company-stock-data-daily-updated")

# Find the csv file
for file in os.listdir(path):
    if file.endswith('.csv'):
        csv_path = os.path.join(path, file)
        break

df = pd.read_csv(csv_path)

# Clean and Transform
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date').drop_duplicates().dropna()
df['SMA_30'] = df['Close'].rolling(30).mean()
df['Daily_Return'] = df['Close'].pct_change()

# Save cleaned data
os.makedirs("data" ,exist_ok=True)
df.to_csv("../data/disney_stock_cleaned.csv", index=False)

print("Data cleaned and saved to data/disney_stock_cleaned.csv")
