class MissingArgError(Exception):
    def __init__(self, arg) -> None:
        self.message = f"Missing arg: '{arg}'"
