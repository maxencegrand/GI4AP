class Word:
    def __init__(self, symbols: tuple[str]):
        """
        Represents a Word
        finite state acceptor.

        :param symbols: symbols n-uple composing the Word
        :type symbols: tuple[str]
        """
        self.__symbols = symbols

    @property
    def words(self):
        return self.__symbols

    def __hash__(self):
        return hash(self.__symbols)

    def __eq__(self, other):
        return self.__symbols == other.symbols

    def __lt__(self, other):
        return self.symbols < other.symbols

    def __gt__(self, other):
        return self.symbols > other.symbols

    def __le__(self, other):
        return self.symbols <= other.symbols

    def __ge__(self, other):
        return self.symbols >= other.symbols

    def __ne__(self, other):
        return self.symbols != other.symbols

    def __str__(self):
        return self.symbols
