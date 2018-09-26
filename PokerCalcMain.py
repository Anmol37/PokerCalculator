from configparser import ConfigParser
import logging.config

from deuces.Card import Card
from deuces.Evaluator import Evaluator
from lib.checkers import input_type_checker

log = logging.getLogger(__name__)


def calculate_deuces(board_arg, hand_arg):
    """
    Calculates the Deuces score as well as its class (high card, pair, etc)
    :param board: list of string with len > 2
    :param hand: list of string with len = 2
    :return: Tuple of (deuces score, deuces class)
    """

    log.debug('Calculating Deuces of {} and {}'.format(board_arg, hand_arg))

    if input_type_checker(board_arg, hand_arg):
        # convert string to Card object
        board = list(map(lambda c: Card.new(c), board_arg))
        hand = list(map(lambda c: Card.new(c), hand_arg))

        evaluator = Evaluator()
        deuces_score = evaluator.evaluate(board, hand)
        deuces_class = evaluator.class_to_string(evaluator.get_rank_class(deuces_score))

        return (deuces_score, deuces_class)

    else:
        log.error('Please see documentation for list of valid input.')


if __name__ == '__main__':
    # load config and initialize logging
    config = ConfigParser()
    config.read('./conf/settings.ini')

    logging.config.fileConfig(disable_existing_loggers=False,
                              fname='./logs/logging_config.ini',
                              defaults={'logfilename': config.get('logs', 'path')})

    board = ['4h', '5h', '8h', '7h', '9c']
    hand = ['2s', '3s']

    print(calculate_deuces(board, hand))

