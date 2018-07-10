class Calc():
    def __init__(self, first, second):
        self.__first = first
        self.__second = second

    def sum_call(self):
        return self.__first + self.__second

    def div_call(self):
        return self.__first / self.__second

    def mult_call(self):
        return self.__first * self.__second

    def sub_call(self):
        return self.__first - self.__second


def main():

    first_value = 100
    second_value = 5

    # Object creation
    calc_run = Calc(first_value, second_value)

    # SUM
    print("Sum  {} + {} is {}".format(first_value, second_value,
                                      calc_run.sum_call()))

    # DIV
    print("Div  {} / {} is {}".format(first_value, second_value,
                                      calc_run.div_call()))

    # MULT
    print("Mult {} * {} is {}".format(first_value, second_value,
                                      calc_run.mult_call()))

    # SUB
    print("Sub  {} - {} is {}".format(first_value, second_value,
                                      calc_run.sub_call()))


if __name__ == '__main__':
    main()
