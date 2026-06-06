import os
from openai import OpenAI
# Gunakan dotenv untuk memuat API Key dari file .env
# from dotenv import load_dotenv
# load_dotenv()

client = OpenAI(api_key="YOUR_API_KEY_HERE")

def get_ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Contoh Integrasi OpenAI (Pastikan API Key sudah diset)")
    # print(get_ai_response("Apa itu Artificial Intelligence?"))
