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
        if response.isdecimal() and int(respopnse) != 0:
            nth = int(response)
            break
        print('please enter a number bigger than 0 or QUIT')
    print()

    if nth == 1:
        print('0')
        print()
        print('the #1 Fibonacci number is 0')
        continue
    