from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

messages = [
    {
        "role": "system",
        "content": """
        You are a cool superhero with sarcasm. 
        Give answers in short 
        NOT long paragraphs
        """
    }
]

print("=" * 50)
print("AI Tutor Started")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\nAI: Goodbye!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:

        response = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile"
        )

        answer = response.choices[0].message.content

        print(f"\nAI: {answer}")

        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:
        print(f"\nError: {e}")