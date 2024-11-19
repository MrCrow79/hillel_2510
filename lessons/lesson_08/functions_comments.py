

# this function.....
def calculate_average(nums_list: list, some_param: str) -> float:
    """ Docstring
    This function is calculate average

    :param nums_list: list of numbers ot floats
    :param some_param: list of numbers ot floats
    :return: float, some description
    """

    return sum(nums_list)/len(nums_list)  # TODO: refactor if len is 0

print(calculate_average([], 'asd'))