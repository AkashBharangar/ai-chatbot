from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

while True:
    user_input = input("\n User:")
    if user_input.lower() == "exit":
        print("AI: GoodBye!!")
        break

    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": """ You are Tony Stark from Marvel Iron Man. Keep in mind all the famous dialogues"""
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        model = "llama-3.3-70b-versatile"
    )

    response = chat_completion.choices[0].message.content

    print("\nAI:", response)