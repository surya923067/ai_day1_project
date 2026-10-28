import os
import requests

# 1. Computer ke environment variable se securely API key uthana
API_KEY = os.environ.get("GEMINI_API_KEY")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

# 2. Payload prepare karna
payload = {
    "contents": [
        {
            "parts": [
                {"text": "In 2 sentences, explain why learning APIs makes software developers high-earning."}
            ]
        }
    ]
}

# 3. Request bhejna
print("🚀 Sending request to Gemini API...")
response = requests.post(URL, json=payload, headers=headers)

# 4. Jawab check karna
if response.status_code == 200:
    data = response.json()
    ai_reply = data['candidates'][0]['content']['parts'][0]['text']
    print("\n🤖 AI Response:\n", ai_reply)
else:
    print(f"\n❌ Error {response.status_code}:", response.text)