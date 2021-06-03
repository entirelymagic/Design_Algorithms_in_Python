def search_unordered_list(list1, searched_values):
    """search an unordered list"""
    for i in range(len(list1)):
        if searched_values == list1[i]:
            return list1[i]
    return None

