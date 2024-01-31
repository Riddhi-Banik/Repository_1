def recurse_highest_num(_list):
    if type(_list) == type(1):
        pass
    elif len(_list) == 1:
        pass
    elif _list[0] <= _list[1]:
        _list = recurse_highest_num(_list[1:])
    else:
        _list.pop(1)

    if len(_list) != 1:
        return _list
    else:
        return recurse_highest_num(_list)


print(recurse_highest_num([2, 8, 3, 7]))