import sys
import argparse
import inferrer
from typing import Set


def read_examples(file: str) -> Set[str]:
    try:
        with open(file, 'r') as f:
            return set(tuple(line.split(',')) for line in f.read().splitlines())
            # return set(line.strip() for line in f)
    except IOError:
        raise Exception('\'{}\' does not exist'.format(file))


def main(args):
    pos_examples = read_examples(args.positive_examples)
    neg_examples = read_examples(args.negative_examples)
    alphabet = inferrer.utils.determine_alphabet(pos_examples.union(neg_examples))
    algorithm = args.algorithm

    if algorithm in ['rpni', 'gold']:
        learner = inferrer.Learner(alphabet=alphabet,
                                   pos_examples=pos_examples,
                                   neg_examples=neg_examples,
                                   algorithm=algorithm)
    elif algorithm in ['lstar', 'nlstar']:
        learner = inferrer.Learner(alphabet=alphabet,
                                   oracle=inferrer.oracle.PassiveOracle(pos_examples,
                                                                        neg_examples),
                                   algorithm=algorithm)

    dfa = learner.learn_grammar()
    print(dfa.to_regex())

    if args.show_dfa:
        dfa.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is the CLI tool for the '
                                                 'grammatical inference library '
                                                 'inferrer. The library tries to'
                                                 ' learn regular languages using '
                                                 'positive and negative example '
                                                 'strings from the target language.')

    parser.add_argument('positive_examples', type=str, metavar='positive-examples',
                        help='Path to the file containing positive example strings, '
                             'i.e. strings that belong in the target language separated '
                             'by newlines.')

    parser.add_argument('negative_examples', type=str, metavar='negative-examples',
                        help='Path to the file containing negative example strings, '
                             'i.e. strings that do not belong in the target language'
                             ' separated by newlines.')

    parser.add_argument('algorithm', type=str,
                        choices=['gold', 'rpni', 'lstar', 'nlstar'],
                        help='The algorithm that should be used to learn the grammar.'
                             ' The options are: gold, rpni, lstar, and nlstar')

    parser.add_argument('--show-dfa', action='store_true',
                        help='If this argument is given, the DFA learned by the '
                             'specified algorithm will be shown.')

    options = parser.parse_args()
    sys.exit(main(options))
