from jarvis.container import (
    ServiceAlreadyRegisteredError,
    ServiceContainer,
    ServiceNotFoundError,
)


class LoggerService:
    """Dummy logger service."""


class TestService:
    """Dummy test service."""


def test_register_and_resolve() -> None:
    container = ServiceContainer()

    logger = object()

    container.register(LoggerService, logger)

    assert container.resolve(LoggerService) is logger


def test_has_service() -> None:
    container = ServiceContainer()

    service = object()

    container.register(TestService, service)

    assert container.has(TestService) is True
    assert container.has(LoggerService) is False


def test_duplicate_registration() -> None:
    container = ServiceContainer()

    container.register(LoggerService, object())

    try:
        container.register(LoggerService, object())
        assert False
    except ServiceAlreadyRegisteredError:
        pass


def test_resolve_missing_service() -> None:
    container = ServiceContainer()

    try:
        container.resolve(LoggerService)
        assert False
    except ServiceNotFoundError:
        pass