# errors

class Error(Exception):
    pass

class DiceError(Error):
    """Raised when an invalid dice value or incorrect dice type is given"""
    pass

class ModError(Error):
    """Raised when invalid mod or an incorrect mod value is given"""
    pass
