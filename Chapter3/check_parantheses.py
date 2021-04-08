from stack_class import Stack


def check_parentheses(parentheses):
    """Given a string of parentheses, check if they close or not"""
    s = Stack()
    they_close = True
    i = 0

    while i < len(parentheses) and they_close:
        p = parentheses[i]
        if p == '(':
            s.push(p)
        elif p == ')':
            if s.its_empty():
                they_close = False
            else:
                s.pop()
        i += 1
    if they_close and s.its_empty():
        return True
    else:
        return False
