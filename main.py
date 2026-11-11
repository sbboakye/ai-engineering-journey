from anthropic import Anthropic
# from dotenv import load_dotenv

def main():
    # load_dotenv()
    client = Anthropic()

    msg = client.messages.create(
        model = "claude-haiku-5-5",
        max_tokens =300,
        messages = [
            {
                "role": "user",
                "content": "Explain Apache Iceberg in two sentences."
            }
        ]
    )
    print(msg)
    print(msg.content[0].text)
    print(msg.usage)

if __name__ == "__main__":
    main()
