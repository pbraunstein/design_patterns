from pubsub.newspaper import Newspaper


class WashingtonPost(Newspaper):
    def __init__(self):
        super(WashingtonPost, self).__init__("Washington Post")

    def update(self, motto):
        print "%s reports that %s said %s" % (
            self.name,
            self.publisher_name,
            motto
        )