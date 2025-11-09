import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# ------------------------------
# Step 1: Create a sample financial dataset
# ------------------------------
data = {
    'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'company_name': ['AlphaCorp', 'BetaTech', 'AlphaCorp', 'BetaTech', 'AlphaCorp',
                     'BetaTech', 'AlphaCorp', 'BetaTech', 'AlphaCorp', 'BetaTech'],
    'sector': ['Finance', 'Technology', 'Finance', 'Technology', 'Finance',
               'Technology', 'Finance', 'Technology', 'Finance', 'Technology'],
    'stock_price': [100, 150, 102, None, 105, 155, 108, 160, np.nan, 165],
    'volume': [1000, 1500, None, 1300, 1200, None, 1100, 1700, 1250, 1800]
}

df = pd.DataFrame(data)

# ------------------------------
# Step 2: Handle missing values
# ------------------------------
df['stock_price'] = df['stock_price'].fillna(df['stock_price'].mean())
df['volume'] = df['volume'].fillna(df['volume'].mean())

# ------------------------------
# Step 3: Create new moving average features (7-day, 30-day)
# ------------------------------
df['MA_7'] = df['stock_price'].rolling(window=7, min_periods=1).mean()
df['MA_30'] = df['stock_price'].rolling(window=30, min_periods=1).mean()

# ------------------------------
# Step 4: Normalize continuous variables using StandardScaler
# ------------------------------
scaler = StandardScaler()
df[['stock_price_scaled', 'volume_scaled', 'MA_7_scaled', 'MA_30_scaled']] = scaler.fit_transform(
    df[['stock_price', 'volume', 'MA_7', 'MA_30']]
)

# ------------------------------
# Step 5: Encode categorical columns (sector, company_name)
# ------------------------------
df_encoded = pd.get_dummies(df, columns=['sector', 'company_name'], drop_first=True)

# ------------------------------
# Step 6: Save cleaned dataset to CSV
# ------------------------------
df_encoded.to_csv("feature_engineered_financial_data.csv", index=False)
print("✅ Cleaned dataset saved as 'feature_engineered_financial_data.csv'")
