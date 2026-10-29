import pandas as pd

print("🚀 Loading raw dataset...")
# 1. Read raw CSV file
df = pd.read_csv("raw_customers.csv")

print("\n--- 🔍 Raw Data ---")
print(df)

# 2. Clean extra whitespace from string columns
df['name'] = df['name'].str.strip()
df['status'] = df['status'].str.strip().str.lower()

# 3. Drop rows where critical data (like email) is missing
cleaned_df = df.dropna(subset=['email']).copy()

# 4. Fill missing dates with a default placeholder
cleaned_df['signup_date'] = cleaned_df['signup_date'].fillna('Unknown')

# 5. Filter only ACTIVE users (essential for targeted AI processing)
active_users = cleaned_df[cleaned_df['status'] == 'active']

print("\n--- ✨ Cleaned & Filtered Active Users ---")
print(active_users)

# 6. Save the clean data to a new CSV file
active_users.to_csv("clean_active_customers.csv", index=False)
print("\n✅ Successfully exported clean data to 'clean_active_customers.csv'!")