def cmmdc(*args: int):
    """Get the lowest common denominator
    """

    for arg in args:
        arg = abs(arg)
        if len(args) > 1:
            next_arg = args[args.index(arg)+1]
            if arg > next_arg:
                return cmmdc(arg-next_arg, next_arg)
            elif next_arg > arg:
                return cmmdc(arg, next_arg-arg)
            else:
                return arg
        else:
            return arg




