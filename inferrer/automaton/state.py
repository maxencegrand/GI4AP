from inferrer.samples import Word

class State:

    def __init__(self, name: Word):
        """
        Represents a State in a
        finite state acceptor.

        :param name: label of the state
        :type name: str
        """
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __hash__(self):
        return hash(self.__name)

    def __eq__(self, other):
        return self.__name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

    def __le__(self, other):
        return self.name <= other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __ne__(self, other):
        return self.name != other.name

    def __str__(self):
        return self.name
