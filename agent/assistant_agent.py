from tools.calculator_tool import CalculatorTool
from tools.file_reader_tool import FileReaderTool
from tools.search_tool import SearchTool


class StudyAssistantAgent:
    """
    Main intelligent agent responsible for:
    - understanding user requests
    - selecting tools
    - generating responses
    """

    def __init__(self):
        self.calculator = CalculatorTool()
        self.file_reader = FileReaderTool()
        self.search_tool = SearchTool()

    def process_request(self, request):
        request_lower = request.lower()

        try:
            # Calculator logic
            if "calculate" in request_lower:
                expression = request_lower.replace("calculate", "").strip()
                result = self.calculator.calculate(expression)
                return f"The result is: {result}"

            # File reading logic
            elif "read file" in request_lower:
                filename = request.split("read file")[-1].strip()
                content = self.file_reader.read_file(filename)
                return f"File content:\n{content}"

            # Search logic
            elif "search" in request_lower:
                keyword = request_lower.replace("search", "").strip()
                result = self.search_tool.search(keyword)
                return result

            else:
                return (
                    "I can help with:\n"
                    "- calculations\n"
                    "- reading files\n"
                    "- searching study notes"
                )

        except Exception as e:
            return f"Error: {str(e)}"