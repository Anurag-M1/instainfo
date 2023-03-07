class instainfoException(Exception):
    """Base exception for this script.

    :note: This exception should not be raised directly."""
    pass


class QueryReturnedBadRequestException(instainfoException):
    pass


class QueryReturnedForbiddenException(instainfoException):
    pass


class ProfileNotExistsException(instainfoException):
    pass


class ProfileHasNoPicsException(instainfoException):
    """
    .. deprecated:: 4.2.2
       Not raised anymore.
    """
    pass


class PrivateProfileNotFollowedException(instainfoException):
    pass


class LoginRequiredException(instainfoException):
    pass


class TwoFactorAuthRequiredException(instainfoException):
    pass


class InvalidArgumentException(instainfoException):
    pass


class BadResponseException(instainfoException):
    pass


class BadCredentialsException(instainfoException):
    pass


class ConnectionException(instainfoException):
    pass


class PostChangedException(instainfoException):
    """.. versionadded:: 4.2.2"""
    pass


class QueryReturnedNotFoundException(ConnectionException):
    pass


class TooManyRequestsException(ConnectionException):
    pass

class IPhoneSupportDisabledException(instainfoException):
    pass

class AbortDownloadException(Exception):
    """
    Exception that is not catched in the error catchers inside the download loop and so aborts the
    download loop.

    This exception is not a subclass of ``instainfoException``.

    .. versionadded:: 4.7
    """
    pass
