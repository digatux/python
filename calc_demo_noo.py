def sum_call(a,b):
    return a + b

def div_call(a,b):
    return a / b

def mult_call(a,b):
    return a * b

def sub_call(a,b):
    return a - b

def main():
    first_value = 100
    second_value = 5

    # Sum
    print("Sum of {} + {} is : {}".format(first_value,second_value,
                                          sum_call(first_value,second_value)))

    # Division
    print("Division of {} / {} is :{}".format(first_value,second_value,
                                              div_call(first_value,second_value)))

    # Multiplication
    print("Multiplication of {} * {} is: {}".format(first_value,second_value,
                                                    mult_call(first_value,second_value)))

    # Subtration
    print("Subtraction {} - {} is {}".format(first_value,second_value,
                                             sub_call(first_value,second_value)))

if __name__ == '__main__':
    main()
