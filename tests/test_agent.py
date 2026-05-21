import unittest
from agent.assistant_agent import StudyAssistantAgent


class TestAgent(unittest.TestCase):

    def test_calculate(self):
        agent = StudyAssistantAgent()
        result = agent.process_request("calculate 10+5")

        self.assertIn("15", result)

    def test_search(self):
        agent = StudyAssistantAgent()
        result = agent.process_request("search python")

        self.assertIn("programming language", result.lower())


if __name__ == "__main__":
    unittest.main()