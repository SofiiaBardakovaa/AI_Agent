class SearchTool:
    """
    Simple keyword-based search tool.
    """

    def __init__(self):
        self.study_data = {
            "python": "Python is a programming language.",
            "ai": "Artificial Intelligence simulates human intelligence.",
            "algorithm": "An algorithm is a step-by-step problem-solving method."
        }

    def search(self, keyword):
        keyword = keyword.lower()

        if keyword in self.study_data:
            return self.study_data[keyword]

        return "No information found."