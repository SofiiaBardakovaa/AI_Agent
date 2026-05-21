from agent.assistant_agent import StudyAssistantAgent


def main():

    assistant = StudyAssistantAgent()

    print("=== AI Study Assistant ===")
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = assistant.process_request(user_input)

        print("\nAssistant:")
        print(response)
        print()


if __name__ == "__main__":
    main()