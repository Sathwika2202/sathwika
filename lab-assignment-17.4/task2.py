import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# ------------------------------
# Step 1: Create a sample sales dataset
# ------------------------------
data = {
    'transaction_id': [201, 202, 203, 204, 205, 206],
    'customer_name': ['John', 'Sarah', 'Alex', 'Maria', 'Tom', 'Lisa'],
    'transaction_date': ['2023/01/15', '2023-02-10', '2023.03.25', '2023-04-12', '2023/05/30', '2023-06-20'],
    'transaction_amount': [1500, -200, 0, 3200, 2800, 4000]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df, "\n")

# ------------------------------
# Step 2: Convert transaction_date to proper datetime format
# ------------------------------
df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')

# ------------------------------
# Step 3: Create a new column "Month-Year" from transaction_date
# ------------------------------
df['Month_Year'] = df['transaction_date'].dt.to_period('M').astype(str)

# ------------------------------
# Step 4: Remove rows with negative or zero transaction amounts
# ------------------------------
df = df[df['transaction_amount'] > 0]

# ------------------------------
# Step 5: Normalize transaction_amount using Min-Max scaling
# ------------------------------
scaler = MinMaxScaler()
df['normalized_amount'] = scaler.fit_transform(df[['transaction_amount']])

# ------------------------------
# Step 6: Display cleaned DataFrame
# ------------------------------
print("Cleaned and Normalized Dataset:\n", df, "\n")

# ------------------------------
# Step 7: Save cleaned dataset to CSV
# ------------------------------
output_path = "cleaned_sales_data.csv"
df.to_csv(output_path, index=False)

print(f"✅ Cleaned dataset saved as '{output_path}'")
