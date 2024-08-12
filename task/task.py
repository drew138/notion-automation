from abc import ABC, abstractmethod


class NotImplementedError(Exception):
    pass


class Task(ABC):

    @abstractmethod
    def run(self) -> None:

        raise NotImplementedError("Method not implemented")
