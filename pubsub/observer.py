from abc import ABCMeta, abstractmethod


class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, motto):
        """
        The current motto to be updated
        """