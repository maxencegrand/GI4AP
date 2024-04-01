class Sample:
    def __init__(self, words: tuple[str]):
        """
        Represents a Word
        finite state acceptor.

        :param words: words n-uple composing the Sample
        :type words: tuple[str]
        """
        self.__words = words

    @property
    def words(self):
        return self.__words

    def __hash__(self):
        return hash(self.__words)

    def __eq__(self, other):
        return self.__words == other.words

    def __lt__(self, other):
        return self.words < other.words

    def __gt__(self, other):
        return self.words > other.words

    def __le__(self, other):
        return self.words <= other.words

    def __ge__(self, other):
        return self.words >= other.words

    def __ne__(self, other):
        return self.words != other.words

    def __str__(self):
        res = "["
        for i, w in enumerate(self.words):
            res += w.__str__()
            if i < len(self.words)-1:
                res += ","
        res += "]"
        return res

    def union(self, other):
        return Sample(self.words.union(other.words))

    def intersection(self, other):
        return Sample(self.words.intersection(other.words))

    def size(self):
        return len(self.words)
