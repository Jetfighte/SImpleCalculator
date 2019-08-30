if __name__ == '__main__':
    def add(num1,num2):
        return str(int(num1) + int(num2))
    def substract(num1,num2):
        return str(int(num1) - int(num2))
    def multiply(num1,num2):
        return str(int(num1) * int(num2))
    def divide(num1,num2):
        return str(int(num1) / int(num2))
    print('Select operation: ')
    print('1.Add')
    print('2.Take Away')
    print('3.Multiply')
    print('4.Divide')
    o = int(0)
    while (o > 0 and o <= 4):
        o = int(input('Chosen operation is(enter number form 1 to 4): '))
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    if o == 1:
        print('Summary of ' + num1 + ' and ' + num2 + ' is ' + add(num1,num2))
    elif o == 2:
        print('Substraction of ' + num1 + ' and ' + num2 + ' is ' + substract(num1,num2))
    elif o == 3:
        print('Multiplication of ' + num1 + ' and ' + num2 + ' is ' + multiply(num1,num2))
    elif o == 4:
        print('Division of ' + num1 + ' and ' + num2 + ' is ' + divide(num1,num2))
    else:
        print('Please, enter a number between 1 and 4')
