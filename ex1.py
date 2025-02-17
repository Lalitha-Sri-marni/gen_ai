import google.generativeai as genai

API_KEY="AIzaSyDgwigPqz-RwiIm8PC_L0VRLw3BiGLCdWA"

genai.configure(api_key=API_KEY)

model=genai.GenerativeModel("gemini-pro")

response=model.generate_content("are you a single?")

print(response.text)