class SearchTool:

    def __init__(self):

        self.database = {
            "python": "Python is a versatile programming language.",
            "ai": "Artificial Intelligence allows machines to simulate human intelligence.",
            "algorithm": "An algorithm is a sequence of steps used to solve a problem."
        }

    def search(self, keyword):

        return self.database.get(
            keyword.lower(),
            "No matching information found."
        )