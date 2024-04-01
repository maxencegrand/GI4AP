class Alphabet:
    def __init__(self, symbols: set[str]):
        """
        Represents a Word
        finite state acceptor.

        :param symbols: symbols set composing the alphabet
        :type symbols: tuple[str]
        """
        self.__symbols = symbols

    @property
    def symbols(self):
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
        res = "["
        for i, s in enumerate(self.symbols):
            res += s.__str__()
            if i < len(self.symbols)-1:
                res += ","
        res += "]"
        return res

    def size(self):
        return len(self.symbols)
