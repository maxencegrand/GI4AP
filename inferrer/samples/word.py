from inferrer.samples import Symbol

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
    def symbols(self):
        return self.__symbols

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __lt__(self, other):
        return self.__str__() < other.__str__()

    def __gt__(self, other):
        return self.__str__() > other.__str__()

    def __le__(self, other):
        return self.__str__() <= other.__str__()

    def __ge__(self, other):
        return self.__str__() >= other.__str__()

    def __ne__(self, other):
        return self.__str__() != other.__str__()

    def __str__(self):
        res = ""
        for s in self.symbols:
            res += s.__str__()
        return res


    def add(self, symbol:Symbol):
        l = list(self.symbols)
        l.append(symbol)
        self.__symbols = tuple(l)
        return self

    def concat(self, other):
        res = Word(self.symbols)
        for s in other.symbols:
            res.add(s)
        return res

    def empty():
        return Word(set())
