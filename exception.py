class UserNotFoundException(Exception):
    detail = "User not found"

class UserUncorrectedPassword(Exception):
    detail = "Password uncorrected"

