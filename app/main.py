from agent import create_agent

def run():
    agent = create_agent()

    print("🤖 AI Assistant (type 'exit' to quit)\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            break

        response = agent.run(query)
        print("AI:", response)

if __name__ == "__main__":
    run()