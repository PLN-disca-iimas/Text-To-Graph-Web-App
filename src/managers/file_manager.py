class FileManager:
    @staticmethod
    def write_file(text: str, filename: str) -> None:
        with open(filename, "w") as output_file:
            output_file.write(str(text))

    @staticmethod
    def read_file(filename: str) -> str:
        with open(filename, "r") as file:
            return file.read()