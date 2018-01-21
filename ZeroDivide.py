def division(divideBy):
    try:
        tmp = 42 / divideBy
        print(tmp)
    except ZeroDivisionError:
       print('Error: Invalid argument!')

division(2)
division(12)
division(0)
division(1)
