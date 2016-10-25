from pubsub.observer import Observer


class WashingtonPost(Observer):
    def __init__(self):
        self.publisher = None
        self.publisher_name = None
        self.name = "Washington Post"

    def set_publisher(self, publisher):
        self.publisher = publisher
        self.publisher.add_observer(self)
        self.publisher_name = publisher.get_name()
        print "%s now following %s" % (
            self.name,
            self.publisher_name
        )

    def update(self, motto):
        print "%s reports that %s said %s" % (
            self.name,
            self.publisher_name,
            motto
        )

    def unfollow(self):
        self.publisher.remove_observer(self)
        self.publisher = None
        self.publisher_name = None
