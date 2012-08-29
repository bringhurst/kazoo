"""Kaoo Exceptions"""
from collections import defaultdict


class KazooException(Exception):
    """Base Kazoo exception that all other kazoo library exceptions inherit
    from"""


class ZookeeperError(KazooException):
    """Base Zookeeper exception for errors originating from the Zookeeper
    server"""


class CancelledError(KazooException):
    """Raised when a process is cancelled by another thread"""


class ConfigurationError(KazooException):
    """Raised if the configuration arguments to an object are invalid"""


class ZookeeperStoppedError(KazooException):
    """Raised when the kazoo client stopped (and thus not connected)"""


class ConnectionDropped(KazooException):
    """ Internal error for jumping out of loops """


class ConnectionClosedError(ZookeeperError):
    """Connection is closed"""


def _invalid_error_code():
    raise RuntimeError('Invalid error code')


EXCEPTIONS = defaultdict(_invalid_error_code)


def _zookeeper_exception(code):
    def decorator(klass):
        def create(*args, **kwargs):
            return klass(args, kwargs)

        EXCEPTIONS[code] = create
        klass.code = code
        return klass

    return decorator


@_zookeeper_exception(0)
class RolledBackError(ZookeeperError):
    pass


@_zookeeper_exception(-1)
class SystemZookeeperError(ZookeeperError):
    pass


@_zookeeper_exception(-2)
class RuntimeInconsistency(ZookeeperError):
    pass


@_zookeeper_exception(-3)
class DataInconsistency(ZookeeperError):
    pass


@_zookeeper_exception(-4)
class ConnectionLoss(ZookeeperError):
    pass


@_zookeeper_exception(-5)
class MarshallingError(ZookeeperError):
    pass


@_zookeeper_exception(-6)
class UnimplementedError(ZookeeperError):
    pass


@_zookeeper_exception(-7)
class OperationTimeoutError(ZookeeperError):
    pass


@_zookeeper_exception(-8)
class BadArgumentsError(ZookeeperError):
    pass


@_zookeeper_exception(-100)
class APIError(ZookeeperError):
    pass


@_zookeeper_exception(-101)
class NoNodeError(ZookeeperError):
    pass


@_zookeeper_exception(-102)
class NoAuthError(ZookeeperError):
    pass


@_zookeeper_exception(-103)
class BadVersionError(ZookeeperError):
    pass


@_zookeeper_exception(-108)
class NoChildrenForEphemeralsError(ZookeeperError):
    pass


@_zookeeper_exception(-110)
class NodeExistsError(ZookeeperError):
    pass


@_zookeeper_exception(-111)
class NotEmptyError(ZookeeperError):
    pass


@_zookeeper_exception(-112)
class SessionExpiredError(ZookeeperError):
    pass


@_zookeeper_exception(-113)
class InvalidCallbackError(ZookeeperError):
    pass


@_zookeeper_exception(-114)
class InvalidACLError(ZookeeperError):
    pass


@_zookeeper_exception(-115)
class AuthFailedError(ZookeeperError):
    pass
