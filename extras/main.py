from ollama import chat
from ollama import ChatResponse

usemodel = "gemma3:270m"
content = "Hello!"
prefix = "/"

usemodel = input("Please type in the name of the model you would like to use: ")
while True:
    content = input("YOU: >>> ")
    if content == prefix + "exit" or content == prefix + "quit":
        break

    response: ChatResponse = chat(
        model=usemodel,
        messages=[
            {
                "role": "user",
                "content": content,
            },
        ],
    )
    print(usemodel + ":", ">>>", response["message"]["content"])

print("Stopping...")
