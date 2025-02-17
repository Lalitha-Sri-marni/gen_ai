import google.generativeai as genai

API_KEY="AIzaSyDgwigPqz-RwiIm8PC_L0VRLw3BiGLCdWA"

genai.configure(api_key=API_KEY)

model=genai.GenerativeModel("gemini-pro")

prompt=input("enter prompt:")

response=model.generate_content(prompt)

print(response.text)