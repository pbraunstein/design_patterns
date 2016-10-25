#!/usr/bin/env python
import sys
sys.path.append('.')

from pubsub.celebrity import Celebrity
from pubsub.washingtonPost import WashingtonPost


def main():
    test_celeb = Celebrity("TestHero", ['1', '2', '3'])
    news = WashingtonPost()
    news.set_publisher(test_celeb)

    test_celeb.scramble_button()
    test_celeb.scramble_button()
    test_celeb.scramble_button()

if __name__ == '__main__':
    main()
