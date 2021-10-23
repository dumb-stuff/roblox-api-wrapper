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
    

class IncorrectPassword(Exception):
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

class InvalidPhoneNumber(Exception):
    """
    Invalid Phone Number
    """
    pass

class PhoneNumberAlreadyAssocidated(Exception):
    """
    Phone Number Already Associdated
    """
    pass

class InvalidCode(Exception):
    """
    Invalid Code
    """
    pass

class RequestEmpty(Exception):
    """
    Request Empty
    """
    pass

class FacebookURLInvalid(Exception):
    """
    Facebook URL Invalid
    """
    pass

class TwitterHandleInvalid(Exception):
    """
    Twitter Handle Invalid
    """
    pass

class YoutubeURLInvalid(Exception):
    """
    Youtube URL Invalid
    """
    pass

class TwitchURLInvalid(Exception):
    """
    Twitch URL Invalid
    """
    pass

class AgeTooLow(Exception):
    """
    Age Too Low
    """
    pass