from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

messages = [
    {
        "role": "system",
        "content": "You are a cool superhero with sarcasm. Give answers in short NOT long paragraphs"
    }
]

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("AI: Goodbye!!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    chat_completion = client.chat.completions.create(
        messages = messages,
        model = "llama-3.3-70b-versatile"
    )

    response = chat_completion.choices[0].message.content

    print("AI:", response)

    messages.append(
        {
            "role":"assitant",
            "content":response
        }
    )