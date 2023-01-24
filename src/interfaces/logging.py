from typing import Protocol


class LoggingProtocol(Protocol):
    def info(self, message: str) -> None:
        ...
