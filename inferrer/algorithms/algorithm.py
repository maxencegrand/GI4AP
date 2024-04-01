import abc
from inferrer import automaton
from typing import Set
from inferrer.samples import Alphabet

class Algorithm(abc.ABC):

    def __init__(self, alphabet: Alphabet):
        """
        :param alphabet: The alphabet (Sigma) of the target
                         regular language.
        :type alphabet: Alphabet
        """
        self._alphabet = alphabet

    @abc.abstractmethod
    def learn(self) -> automaton.FSA:
        """
        Attempts to learn the grammar of the target
        regular language by using the sets of positive
        and negative example strings. The method returns
        a DFA that is consistent with the sample.
        Known implementations are:
        Gold
        RPNI
        Angluin Learning (L*)
        NL*

        :return: DFA consistent with the sample.
        :rtype: Automaton
        """
        pass
