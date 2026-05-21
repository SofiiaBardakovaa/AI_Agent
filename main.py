from agent.assistant_agent import StudyAssistantAgent

def main():
    agent = StudyAssistantAgent()

    print("=== AI Study Assistant ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = agent.process_request(user_input)
        print(f"\nAssistant: {response}\n")


if __name__ == "__main__":
    main()