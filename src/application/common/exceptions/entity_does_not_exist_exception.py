class EntityDoesNotExistException(Exception):
    def __init__(self, entity_name: str, entity_id: int):
        super().__init__(f"{entity_name} with id {entity_id} does not exist")
