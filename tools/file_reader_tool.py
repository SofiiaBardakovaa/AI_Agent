class FileReaderTool:

    def read_file(self, filepath):

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()

        except FileNotFoundError:
            raise FileNotFoundError("File not found")