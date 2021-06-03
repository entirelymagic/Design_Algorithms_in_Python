def search_unordered_list(list1, searched_value):
    """Search an unordered list
    Complexity for the algorithm is 'O(n)' and it is resulted from the 'for loop' and the length 'n' of the list.
    """

    for i in range(len(list1)):
        if searched_value == list1[i]:
            return i
    return None


def search_ordered_list(list1, searched_value):
    """Search an ordered list
    Complexity for the algorithm is 'O(n)' and it is resulted from the 'for loop' and the length 'n' of the list.
    """

    if searched_value < list1[0] or searched_value > list1[-1]:
        return None
    for i in range(len(list1)):
        if searched_value == list1[i]:
            return i
        elif searched_value < list1[i]:
            return None
    return None



