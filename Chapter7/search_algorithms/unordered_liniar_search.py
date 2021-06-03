def search_unordered_list(list1, searched_values):
    """Search an unordered list
    Complexity for the algorithm is 'O(n)' and it is resulted from the 'for loop' and the length 'n' of the list.
    """
    for i in range(len(list1)):
        if searched_values == list1[i]:
            return list1[i]
    return None

