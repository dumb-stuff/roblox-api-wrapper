class PlatformException(Exception):
    """
    When an error occurs in the platform.
    """
    pass

class InvalidRequest(Exception):
    """
    Invalid Request are raised when the request is invalid.
    """
    pass

class AssetNotFound(Exception):
    """
    When an asset is not found.
    """
    pass

class InternalServerError(Exception):
    """
    When an internal server error occurs.
    """
    pass

class BadGateway(Exception):
    """
    When a bad gateway occurs.
    """
    pass

class ApplicationException(Exception):
    """
    When an token is likely wrong.
    """
    pass

class Forbidden(Exception):
    """
    When a request is forbidden.
    """
    pass

class BadRequest(Exception):
    """
    When a request is invalid.
    """
    pass