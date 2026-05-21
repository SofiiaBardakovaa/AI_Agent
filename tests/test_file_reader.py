import unittest
from tools.file_reader_tool import FileReaderTool


class TestFileReader(unittest.TestCase):

    def test_file_not_found(self):
        reader = FileReaderTool()

        with self.assertRaises(FileNotFoundError):
            reader.read_file("missing.txt")


if __name__ == "__main__":
    unittest.main()