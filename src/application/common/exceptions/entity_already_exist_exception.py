class EntityAlreadyExistException(Exception):
    def __init__(self, field: str):
        super().__init__(f"Such {field} already exist.")
