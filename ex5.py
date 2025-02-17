import google.generativeai as genai

from dotenv import load_dotenv

import os

load_dotenv()

ApI_key=os.getenv("GEMINI_AI_API")

genai.configure(api_key=API_KEY)

model=genai.GenerativeModel("gemini-pro")

prompt=input("enter prompt:")

response=model.generate_content(prompt)

print(response.text)