# Create Auth.py under Services folder

class Auth:
    @staticmethod
    def user(authMethod: str, token: str) -> int:
        # Implement your logic here
        if authMethod == "google":
            return 1
        elif authMethod == "facebook":
            return 2
        elif authMethod == "twitter":
            return 3
        else:
            return 0
