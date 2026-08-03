from ollama import chat

response = chat(
    model="qwen2.5vl:3b",
    messages=[
        {
            "role": "user",
            "content": "Describe this image.",
            "images": [
                r"C:\Users\srija\AppData\Local\Temp\jarvis\screenshots\20260803_201852.png"
            ],
        }
    ],
)

print(response.message.content)