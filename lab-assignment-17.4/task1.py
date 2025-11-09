import pandas as pd
import numpy as np

# ------------------------------
# Step 1: Create a sample dataset
# ------------------------------
data = {
    'employee_id': [101, 102, 103, 104, 105, 106],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'salary': [50000, np.nan, 62000, 58000, None, 54000],
    'department': ['HR', 'hr', 'Human Resources', 'IT', None, 'Finance'],
    'job_role': ['Manager', 'Developer', 'Analyst', 'Developer', 'Manager', None],
    'joining_date': ['2020/05/01', '2021-03-15', None, '2019.07.10', '2020-12-01', '2018/11/25']
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df, "\n")

# ------------------------------
# Step 2: Handle missing values
# ------------------------------
df['salary'] = df['salary'].fillna(df['salary'].mean())  # Replace missing salary with mean
df['department'] = df['department'].fillna('Unknown')    # Replace missing department
df['joining_date'] = df['joining_date'].fillna('2000-01-01')  # Default date

# ------------------------------
# Step 3: Convert joining_date to datetime
# ------------------------------
df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')

# ------------------------------
# Step 4: Standardize department names
# ------------------------------
def standardize_department(dept):
    if pd.isna(dept):
        return 'Unknown'
    dept = dept.strip().lower()
    if dept in ['hr', 'human resources']:
        return 'HR'
    elif dept in ['it', 'information technology']:
        return 'IT'
    elif dept in ['finance']:
        return 'Finance'
    elif dept in ['unknown']:
        return 'Unknown'
    else:
        return 'Other'

df['department'] = df['department'].apply(standardize_department)

# ------------------------------
# Step 5: Encode categorical variables
# ------------------------------
df_encoded = pd.get_dummies(df, columns=['department', 'job_role'], drop_first=True)

# ------------------------------
# Step 6: Display cleaned DataFrame
# ------------------------------
print("Cleaned and Encoded Dataset:\n", df_encoded, "\n")

# ------------------------------
# Step 7: Save cleaned dataset to CSV
# ------------------------------
output_path = "cleaned_employee_data.csv"
df_encoded.to_csv(output_path, index=False)

print(f"✅ Cleaned dataset saved as '{output_path}'")
