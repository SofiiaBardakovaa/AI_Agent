import google.generativeai as genai
import os
from dotenv import load_dotenv

from tools.calculator_tool import CalculatorTool
from tools.file_reader_tool import FileReaderTool
from tools.search_tool import SearchTool

load_dotenv()


class StudyAssistantAgent:
    """
        AI-powered assistant agent that processes user requests
        and uses external tools when needed.
        """
    def __init__(self):

        # Configure Gemini
        api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

        # Tools
        self.calculator = CalculatorTool()
        self.file_reader = FileReaderTool()
        self.search_tool = SearchTool()

    def process_request(self, user_input):

        user_input_lower = user_input.lower()

        try:

            # TOOL 1: Calculator
            if "calculate" in user_input_lower:

                expression = user_input_lower.replace("calculate", "").strip()

                result = self.calculator.calculate(expression)

                prompt = (
                    f"Explain this math result simply.\n"
                    f"Expression: {expression}\n"
                    f"Result: {result}"
                )

                response = self.model.generate_content(prompt)

                return response.text

            # TOOL 2: File Reader
            elif "read file" in user_input_lower:

                filename = user_input.split("read file")[-1].strip()

                content = self.file_reader.read_file(filename)

                prompt = (
                    "Summarize these study notes:\n\n"
                    f"{content}"
                )

                response = self.model.generate_content(prompt)

                return response.text

            # TOOL 3: Search
            elif "search" in user_input_lower:

                keyword = user_input_lower.replace("search", "").strip()

                search_result = self.search_tool.search(keyword)

                prompt = (
                    f"Using this information:\n"
                    f"{search_result}\n\n"
                    f"Provide a helpful explanation for a student."
                )

                response = self.model.generate_content(prompt)

                return response.text

            else:

                general_response = self.model.generate_content(user_input)

                return general_response.text

        except Exception as e:
            return f"Error: {str(e)}"