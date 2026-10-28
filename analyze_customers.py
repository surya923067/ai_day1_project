import os
import pandas as pd
import requests

# 1. Check if cleaned CSV file exists
if not os.path.exists("clean_active_customers.csv"):
  print(
      "❌ Error: 'clean_active_customers.csv' nahi mili! Pehle 'python"
      " clean_data.py' run karein."
  )
  exit()

print("📂 Loading cleaned customer data...")
df = pd.read_csv("clean_active_customers.csv")
csv_data_string = df.to_string(index=False)

# 2. Configuration for Gemini API
API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY"  # Yahan apni asli API key daalein

if API_KEY == "YOUR_ACTUAL_GEMINI_API_KEY":
  print(
      "❌ Error: Aapne code mein apni asli API key nahi dali hai! Kripya"
      " 'YOUR_ACTUAL_GEMINI_API_KEY' ko replace karein."
  )
  exit()

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={API_KEY}"
headers = {"Content-Type": "application/json"}

# 3. Build the prompt
prompt = f"""
You are an expert AI data analyst. Here is our active customer dataset:

{csv_data_string}

Please analyze this data and provide:
1. A brief summary of the customer base.
2. Two actionable business insights based on their signup dates and names.
"""

payload = {"contents": [{"parts": [{"text": prompt}]}]}

# 4. Send request and handle response safely
print("🚀 Sending cleaned data prompt to Gemini API...")
response = requests.post(URL, json=payload, headers=headers)

if response.status_code == 200:
  data = response.json()
  try:
    ai_reply = data["candidates"][0]["content"]["parts"][0]["text"]
    print("\n🤖 AI Data Analysis Response:\n", ai_reply)
  except (KeyError, IndexError):
    print(
        "\n⚠️ API response structure unexpected. Full response received:", data
    )
else:
  print(f"\n❌ API Error {response.status_code}:", response.text)