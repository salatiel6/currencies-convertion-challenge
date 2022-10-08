class MissingArgError(Exception):
    """
    Exception that handles requests without the necessaries url query arguments
    """
    def __init__(self, arg) -> None:
        self.message = f"Missing arg: '{arg}'"
