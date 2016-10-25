from abc import ABCMeta

from pubsub.observer import Observer

class Newspaper(Observer):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.publisher = None
        self.publisher_name = None
        self.name = name

    def set_publisher(self, publisher):
        self.publisher = publisher
        self.publisher.add_observer(self)
        self.publisher_name = publisher.get_name()
        print "%s now following %s" % (
            self.name,
            self.publisher_name
        )

    def unfollow(self):
        self.publisher.remove_observer(self)
        self.publisher = None
        self.publisher_name = None
