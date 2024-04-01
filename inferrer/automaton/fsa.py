import abc
from inferrer import automaton
from inferrer.samples import Alphabet, Word
from typing import Set, Tuple


class FSA(abc.ABC):
    """
    Represents a finite state acceptor that
    accepts or rejects strings of the given
    alphabet.

    The two known implementations of this
    abstract class is dfa.py and nfa.py.
    """
    def __init__(self, alphabet: Alphabet):
        if '' in alphabet.symbols:
            raise ValueError('The empty string is not allowed in the alphabet!')
        self.__alphabet = alphabet

    @property
    def alphabet(self):
        return self.__alphabet

    @abc.abstractmethod
    def parse_string(self, w: Word) -> Tuple[automaton.State, bool]:
        """
        Parses each symbol of the input word through
        the finite state acceptor.

        :param s: The string to parse (s element of alphabet*)
        :type s: str
        :return: The state after reading the string s and whether
                 the fsa accepted the input string.
        :rtype: tuple(State, bool)
        """
        pass
