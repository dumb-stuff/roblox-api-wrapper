from types import prepare_class


class PlatformException(Exception):
    """
    When an error occurs in the platform.
    """
    

class InvalidRequest(Exception):
    """
    Invalid Request are raised when the request is invalid.
    """
    

class AssetNotFound(Exception):
    """
    When an asset is not found.
    """
    

class InternalServerError(Exception):
    """
    When an internal server error occurs.
    """
    

class BadGateway(Exception):
    """
    When a bad gateway occurs.
    """
    

class ApplicationException(Exception):
    """
    When an token is likely wrong.
    """
    

class Forbidden(Exception):
    """
    When a request is forbidden.
    """
    

class BadRequest(Exception):
    """
    When a request is invalid.
    """
    

class UserNotFound(Exception):
    """
    When a user is not found.
    """
    

class InvalidCredential(Exception):
    """
    When a credential is invalid.
    """
    

class InvalidBirthday(Exception):
    """
    When a birthday is invalid.
    """
    

class AuthorizationDenied(Exception):
    """
    When a user is not authorized.
    """
    

class TokenValidationFailed(Exception):
    """
    When a token is invalid.
    """
    

class PinIsLocked(Exception):
    """
    When a pin is locked.
    """
    

class InvalidBirthdateChange(Exception):
    """
    When a birthday is invalid.
    """
    

class UnknownError(Exception):
    """
    When an unknown error occurs.
    """
    

class InvalidRequestMethodError(Exception):
    """
    When an invalid request method is used.
    """
    

class FeatureDisabled(Exception):
    """
    When a feature is disabled.
    """
    

class UnknownGender(Exception):
    """
    When an unknown gender isn't on list
    """
    

class NotConnectedToXboxLive(Exception):
    """
    When user didn't connect roblox account to xbox live
    """
    

class Incorrectword(Exception):
    """
    When user type wrong word
    """
    
class PhoneNumberNotFound(Exception):
    """
    Phone Number NotFound
    """

class Flooded(Exception):
    """
    Flooded
    """