import os

api_key = os.environ.get("API_KEY")

if api_key:
    print(f"API key: {api_key}")
else:
    print("API key is not set.")
