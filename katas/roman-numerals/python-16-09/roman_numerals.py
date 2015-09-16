ONE = 'I'
FIVE = 'V'
TEN = 'X'


class Roman(object):

    @classmethod
    def translate(cls, number):
        if number > 13:
            remaining = (number - 10)
            return TEN + cls._roman_around_five(remaining)
        if number > 8:
            return cls._roman_around_ten(number)
        if number > 3:
            return cls._roman_around_five(number)

        return number * ONE

    @classmethod
    def _roman_around_five(cls, number):
        return ((5 - number) * ONE) + FIVE + ((number - 5) * ONE)

    @classmethod
    def _roman_around_ten(cls, number):
        return ((10 - number) * ONE) + TEN + ((number - 10) * ONE)
