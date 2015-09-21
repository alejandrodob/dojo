ONE = 'I'
FIVE = 'V'
TEN = 'X'

ONE_VALUE = 1
FIVE_VALUE = 5
TEN_VALUE = 10


class Roman(object):

    @classmethod
    def translate(cls, number):
        if number >= TEN_VALUE:
            return TEN
        if number == (TEN_VALUE - ONE_VALUE):
            return ONE + TEN
        if number >= FIVE_VALUE:
            return FIVE + (number - FIVE_VALUE) * ONE
        if number >= (FIVE_VALUE - ONE_VALUE):
            return ONE + FIVE
        return number * ONE
