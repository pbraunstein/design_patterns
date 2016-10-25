#!/usr/bin/env python
import sys
sys.path.append('.')

from pubsub.celebrity import Celebrity
from pubsub.buzzfeed import Buzzfeed
from pubsub.washingtonPost import WashingtonPost
from pubsub.wsj import Wsj


def main():
    beethoven = Celebrity("Beethoven", [
        'I want to seize fate by the throat',
        'Music is a higher revelation than all wisdom and philosophy',
        'Must it be? It must be'
    ])
    news1 = WashingtonPost()
    news2 = Buzzfeed()
    news3 = Wsj()
    news1.set_publisher(beethoven)
    news2.set_publisher(beethoven)
    print

    beethoven.change_of_heart()
    print

    news3.set_publisher(beethoven)
    print

    beethoven.change_of_heart()
    print

    news1.unfollow()
    news3.unfollow()
    print

    beethoven.change_of_heart()
    print

if __name__ == '__main__':
    main()
