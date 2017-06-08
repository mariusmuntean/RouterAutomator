from abc import ABC, abstractmethod


class BaseGeckoDriverCopy(ABC):
    @abstractmethod
    def copy(self):
        pass
