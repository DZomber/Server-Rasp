def cantidad_ceros(*args):
    ceros = 0
    for arg in args:
        if ceros + 1 == len(args):
            return False
        elif arg[ceros] == 0 and arg[ceros + 1] == 0:
            return True
        else:
            ceros += 1
    return False


cantidad_ceros(6, 1, 5, 1, 0, 3, 0, 1)

