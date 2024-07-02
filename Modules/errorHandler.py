# Error Handling
class NoMatchingNameError(Exception):
    def __init__(self, name):
        self.name = name 
        self.message = f'No matching name: {name}'
        super().__init__(self.message)

class NoMatchingIDError(Exception):
    def __init__(self, ID):
        self.ID = ID 
        self.message = f'No matching ID: {ID}'
        super().__init__(self.message)

class AuthenticationError(Exception):
    def __init__(self):
        self.message = f'Authentication Error'
        super().__init__(self.message)