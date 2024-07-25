class EntityDontMatchPasswordException(Exception):
    def __init__(self):
        super().__init__("The passwords don't match")


class EntityInvalidCredentialsException(Exception):
    pass
