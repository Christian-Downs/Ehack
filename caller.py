from openai import OpenAI
client = OpenAI()



def caller(prompt, system = None):
    messages = [

        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Hello"
            }
        ]
        },
        {
        "role": "assistant",
        "content": [
            {
            "type": "text",
            "text": "Hello! How can I assist you today?"
            }
        ]
        }
    ]

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= messages,
    response_format={
        "type": "text"
    },
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )


