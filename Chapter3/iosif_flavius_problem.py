from Chapter3.queue_class import Queue


def game(listName, steps) -> 'Queue':
    """
    More then 2 person get in line. After a number of steps, each of them, the first person goes
    back to the end of the line. The first person is now eliminated from the queue.
    Again after a number of steps, the first person goes back to the end of the line.
    The first person in line is now eliminated from the queue.
    The operation is repeated until one person is left on the line.
    The person that remains in line is returned at the end.

    :param listName:
    :param steps:
    :return last person from the list:
    """
    game_queue = Queue()

    for person in listName:
        game_queue.add(person)

    while game_queue.length() > 1:
        for i in range(steps):
            game_queue.add(game_queue.remove())
        game_queue.remove()
    return game_queue


list_of_names = ['Ana', 'Madalina', 'Cecilia', 'Elvis', 'Alex', 'Dan']
steps = 6
x = (game(list_of_names, steps))
print(game(list_of_names, steps))
print(x)