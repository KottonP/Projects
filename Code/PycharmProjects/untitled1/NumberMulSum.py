while True:
    x = input("Give integer: ")
    y = input("Give integer: ")

    while True:
        if (x.isdigit()) and (y.isdigit()):
            print('----------------')
            print('x+y={} | xy={}'.format(int(x)+int(y), int(x)*int(y)))
            i = input('Shall I continue? \n'
                      'YES to proceed \n'
                      'STOP for exit.\n')
            if i == 'YES':
                x = input("Give integer: ")
                y = input("Give integer: ")
                continue
            elif i == 'STOP':
                print('Goodbye.')
                break
        else:
            print('Give integers only!')
            x = "0"
            y = "0"
            break
    break
