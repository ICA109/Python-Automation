def collatz(number):
    if number % 2 == 0:
        tmp = number
        print(tmp)
        return tmp
    else:
        tmp = 3 * number + 1
        print(tmp)
        return tmp


try:
    print('Enter number:')
    userInput = int(input())
    tentativeResult = collatz(userInput)
    while True:
        if tentativeResult == 1:
            break
        else:
            tentativeResult = collatz(tentativeResult)
except ValueError:
    print('Error. Must enter an integer!')

