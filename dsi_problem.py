def eval():
    while True:
        try:
            x = int(input('Please enter a number: '))
            y = int(input('Please enter a number: '))
            return x == y
        except ValueError:
            print('That is not a number, Try Again')
result = eval()
print(result)
