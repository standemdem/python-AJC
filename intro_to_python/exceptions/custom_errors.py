class CustomError(Exception):
    def __init__(self, message):
        self.message = message

    def printError(self):
        return f"CustomError: {self.message}\n\nCustom documentation: This is a custom error with additional information."
    

class AnotherError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"AnotherError: {self.message}\n\nCustom documentation: This is a custom error with additional information."