

number = '$750K'

number_result = number[1:-1].replace('.', '')
if (number[-1] == 'M'):
    print("{:0<7d}".format(int(number_result)))
elif (number[-1] == 'K'):
    print("{:0<6d}".format(int(number_result)))
