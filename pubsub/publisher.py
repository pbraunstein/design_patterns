from abc import ABCMeta, abstractmethod


class Publisher:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_name(self):
        """
        Each child must implement this
        """

    @abstractmethod
    def notify_observers(self):
        """
        Each child must implement this
        """

    @abstractmethod
    def add_observer(self, observer):
        """
        Each child must implement this
        """

    @abstractmethod
    def remove_observer(self, observer):
        """
        Each child must implement this
        """
