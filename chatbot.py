import  google.generativeai as genai
key = "AIzaSyC40bfpXgGvPq1PVhlDsU-eJuD4dIjb6XQ"
print(key)

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")
while True:
    user = input("enter what you want to tell or type exit to close\n")
    if user.lower() == "exit":
        print("bye bye")
        break
    response = model.generate_content(user)
    print("BOT: ", response.text)

