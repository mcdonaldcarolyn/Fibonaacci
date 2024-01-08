import sys

print (" Fibonacci sequence by inventwithpython.com")

while True:
    while True:
        print('Enter the Nth Fibonacci number you wish to')
        print('calculate (such as 5, 50, 100), or QUIT to quit:')
        response = input('> ').upper()

        if response == 'QUIT':
            print('Thanks for playing')
            sys.exit()
        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break
        print('please enter a number bigger than 0 or QUIT')
    print()

    if nth == 1:
        print('0')
        print()
        print('the #1 Fibonacci number is 0')
        continue
    elif nth ==2:
        print('0,1')
        print ()
        print('the #2 Fibonacci number is 1')
        continue
    
    if nth == 10000:
        print('WARNING this will take awhile')
        print(' you may want to quit, press Ctrl-C')
        input ('press enter to begin')

    secondToLastNumber = 0 
    lastNUmber = 1 
    fibNumbersCalculated = 2
    print('0, 1, ', end='')

    while True:
        nextNumber = secondToLastNumber + lastNUmber
        fibNumbersCalculated += 1
        print(nextNumber, end='')

        if fibNumbersCalculated == nth:
            print()
            print()
            print(' the #', fibNumbersCaculated, ' Fibinacci', 'number is', nextNumber, sep='')
            break

        print(', ', end='')

        secondToLastNumber = lastNumber
        lastNumber = nextNumber 


    