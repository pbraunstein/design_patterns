from pubsub.newspaper import Newspaper


class Buzzfeed(Newspaper):
    def __init__(self):
        super(Buzzfeed, self).__init__('Buzzfeed')

    def update(self, motto):
        print "You won't believe what %s said. Check out %s (%s)" % (
            self.publisher_name,
            self.name,
            motto
        )
