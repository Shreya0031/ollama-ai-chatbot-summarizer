import ollama
from scraper import fetch_website_contents

print("🤖 AI Chatbot started! Type 'exit' to stop.\n")

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Chat ended.")
        break

    # 🔥 Special command for scraping
    if user_input.startswith("summarize "):
        url = user_input.replace("summarize ", "")
        content = fetch_website_contents(url)

        messages.append({
            "role": "user",
            "content": f"Summarize this website:\n{content[:2000]}"
        })
    else:
        messages.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model="llama3",
        messages=messages
    )

    ai_reply = response['message']['content']
    messages.append({"role": "assistant", "content": ai_reply})

    print("AI:", ai_reply)