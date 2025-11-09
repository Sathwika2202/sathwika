import pandas as pd
import numpy as np

# ------------------------------
# Step 1: Create a sample healthcare dataset
# ------------------------------
data = {
    'patient_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'gender': ['M', 'Female', 'male', 'F', 'Male', 'm'],
    'age': [25, 40, 35, 60, 55, 50],
    'height_cm': [165, 170, None, 180, 160, 175],
    'weight_kg': [60, 75, 70, None, 55, 80],
    'blood_pressure': [120, np.nan, 130, 125, None, 118],
    'heart_rate': [80, 76, None, 90, 88, np.nan]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df, "\n")

# ------------------------------
# Step 2: Fill missing numeric values with column mean
# ------------------------------
numeric_cols = ['height_cm', 'weight_kg', 'blood_pressure', 'heart_rate']
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# ------------------------------
# Step 3: Standardize height (convert cm to meters)
# ------------------------------
df['height_m'] = df['height_cm'] / 100

# ------------------------------
# Step 4: Correct inconsistent gender labels
# ------------------------------
def clean_gender(g):
    if pd.isna(g):
        return 'Unknown'
    g = g.strip().lower()
    if g in ['m', 'male']:
        return 'Male'
    elif g in ['f', 'female']:
        return 'Female'
    else:
        return 'Other'

df['gender'] = df['gender'].apply(clean_gender)

# ------------------------------
# Step 5: Drop irrelevant columns (patient_id, height_cm)
# ------------------------------
df_cleaned = df.drop(columns=['patient_id', 'height_cm'])

# ------------------------------
# Step 6: Display cleaned dataset
# ------------------------------
print("Cleaned Healthcare Dataset:\n", df_cleaned, "\n")

# ------------------------------
# Step 7: Save cleaned dataset to CSV
# ------------------------------
output_path = "cleaned_healthcare_data.csv"
df_cleaned.to_csv(output_path, index=False)

print(f"✅ Cleaned dataset saved as '{output_path}'")
