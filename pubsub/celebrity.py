from random import choice

from pubsub.publisher import Publisher


class Celebrity(Publisher):
    EMPTY_SAYING = 'I have nothing to say'

    def __init__(self, name, sayings):
        self.name = name
        self.sayings = sayings
        self.newspapers = set()
        self.current_moto = None
        self._choose_motto()

    def get_name(self):
        return self.name

    def scramble_button(self):
        """
        Makes the celebrity change his/her motto and update subscribers
        """
        self._choose_motto()
        self.notify_observers()

    def notify_observers(self):
        for to_notify in self.newspapers:
            to_notify.update(self.current_motto)

    def add_observer(self, observer):
        self.newspapers.add(observer)

    def remove_observer(self, observer):
        """
        Idempotent - if observer passed isn't observing, no-op
        """
        self.newspapers.discard(observer)

    def _choose_motto(self):
        try:
            self.current_motto = choice(self.sayings)
        except IndexError:
            self.current_motto = self.EMPTY_SAYING
