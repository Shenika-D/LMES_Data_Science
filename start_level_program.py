import pandas as pd

# Load the dataset
df = pd.read_csv("World happiness report.csv")

# Display basic info
print("\n--- Dataset Info ---")
print(df.info())

# Show first 5 rows
print("\n--- First 5 Rows ---")
print(df.head())

# Column names
print("\n--- Column Names ---")
print(df.columns.tolist())

# Rename columns for easier use
df.rename(columns=lambda x: x.strip().replace("\t", ""), inplace=True)

# Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Summary statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# Data types
print("\n--- Data Types ---")
print(df.dtypes)

# Check unique values in categorical column
print("\n--- Unique Countries ---")
print(df["Country name"].nunique())

# Correlation matrix (optional for insights)
print("\n--- Correlation Matrix ---")
print(df.corr(numeric_only=True))

# Sampling - simple random sample of 10 records
sample_random = df.sample(n=10, random_state=1)
print("\n--- Random Sample (10 records) ---")
print(sample_random)

# Sampling - 20% of the dataset
sample_fraction = df.sample(frac=0.2, random_state=42)
print("\n--- Sample 20% of Dataset ---")
print(sample_fraction)

# Save the sampled data to a new file (optional)
sample_random.to_csv("sample_random.csv", index=False)
sample_fraction.to_csv("sample_fraction.csv", index=False)

print("\n Data operations completed up to sampling.")
