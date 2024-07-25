class EntityIncorrectFormatException(Exception):
    def __init__(self, field: str):
        super().__init__(f"Incorrect {field} format.")
