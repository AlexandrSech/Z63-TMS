import operator


def zero(operator=None): #your code here
    _self = 0
    return _self if operator is None else operator(_self)


def one(operator=None): #your code here
    _self = 1
    return _self if operator is None else operator(_self)


def two(operator=None): #your code here
    _self = 2
    return _self if operator is None else operator(_self)


def three(operator=None): #your code here
    _self = 3
    return _self if operator is None else operator(_self)


def four(operator=None): #your code here
    _self = 4
    return _self if operator is None else operator(_self)


def five(operator=None): #your code here
    _self = 5
    return _self if operator is None else operator(_self)


def six(operator=None): #your code here
    _self = 6
    return _self if operator is None else operator(_self)


def seven(operator=None): #your code here
    _self = 7
    return _self if operator is None else operator(_self)


def eight(operator=None): #your code here
    _self = 8
    return _self if operator is None else operator(_self)


def nine(operator=None): #your code here
    _self = 9
    return _self if operator is None else operator(_self)


def plus(number): #your code here
    def plus_(y):
        return operator.add(y, number)
    return plus_

    # return lambda y: operator.add(y, number)


def minus(number): #your code here
    def minus_(y):
        return operator.sub(y, number)
    return minus_


def times(number): #your code here
    def times_(y):
        return operator.mul(y, number)
    return times_


def divided_by(number): #your code here
    def divided_by_(y):
        return operator.floordiv(y, number)
    return divided_by_


if __name__ == "__main__":
    print(nine(plus(nine())))
    print(nine(minus(nine())))
    print(zero(minus(nine())))
    print(two(minus(eight())))
