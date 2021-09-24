class InvalidCountError(Exception):
    def __init__(self, message):
        super().__init__(message)       # super().__init__