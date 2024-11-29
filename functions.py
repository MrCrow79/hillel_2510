from loggers import sample_logger
from loggers import logger_from_file
import logging



def factorial(n):
    sample_logger.info(f'Getting factorial for {n}')
    logging.info(f'Getting factorial for {n}')

    if type(n) != int:
        error_text = f'Only int allowed, you put {type(n)}'
        sample_logger.error(f'Getting factorial for {n}')
        sample_logger.error(error_text)
        raise TypeError(error_text)

    if n < 0:
        error_text = f'You have to use 0 or positive numbers. You put {n}'
        sample_logger.error(f'Getting factorial for {n}')
        sample_logger.error(error_text)
        raise ValueError(error_text)

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_anagram(word1, word2):
    """
    description
    """
    return sorted(word1) == sorted(word2)


def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]


def find_primes(n: int) -> list:

    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def triangle_area(a, b, c):
    # if a + b <= c or a + c <= b or b + c <= a:
    #     return 0
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def convert_to_24_hour(time_str):

    logger_from_file.info(f'Start using {__name__}')
    logger_from_file.debug(f'input value {time_str}')

    if type(time_str) == list:
        logger_from_file.error(f'type is incorrect, expected str but have {type(time_str)}')
        raise TypeError

    if type(time_str) == dict:
        logger_from_file.error(f'type is incorrect, expected str but have {type(time_str)}')
        raise ValueError

    logger_from_file.debug(f'Splitting')
    parts = time_str.split()

    if len(parts) != 2:
        logger_from_file.error('Time format is not a `hh:mm period`')
        raise ValueError('Time format is not a `hh:mm period`')

    time, period = parts

    logger_from_file.debug(f'Get parts, {time}, {period}')

    hours, minutes = map(int, time.split(':'))

    logger_from_file.debug(f'Get hours, minuets: {hours}, {minutes}')
    if period.lower() == 'pm' and hours != 12:
        hours += 12
    elif period.lower() == 'am' and hours == 12:
        hours = 0
    result = f'{hours:02}:{minutes:02}'
    logger_from_file.debug(f'done, return {result}')

    return result


if __name__ == '__main__':
    print('some info from fuctions file')