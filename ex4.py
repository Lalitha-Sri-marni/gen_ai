import google.generativeai as genai

API_KEY = "AIzaSyDgwigPqz-RwiIm8PC_L0VRLw3BiGLCdWA"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")

while True:
    prompt = input("Enter prompt (or type 'exit' to quit): ")
    if prompt.lower() == "exit":
        print("Exiting...")
        break
    
    response = model.generate_content(prompt)
    print(response.text)
