ROMAN_ONE = 'I'
ROMAN_FIVE = 'V'
ROMAN_TEN = 'X'

FIVE = 5
TEN = 10

class Roman(object):

    @classmethod
    def translate(cls, number):
        if number == 19:
            return ROMAN_TEN + ROMAN_ONE + ROMAN_TEN
        if cls._is_around_fifteen(number):
            number = number - TEN
            return ROMAN_TEN + (FIVE - number) * ROMAN_ONE + ROMAN_FIVE + (number - FIVE) * ROMAN_ONE
        if cls._is_around_ten(number):
            return (TEN - number) * ROMAN_ONE + ROMAN_TEN + (number - TEN) * ROMAN_ONE
        if cls._is_around_five(number):
            return (FIVE - number) * ROMAN_ONE + ROMAN_FIVE + (number - FIVE) * ROMAN_ONE
        return ROMAN_ONE * number

    @classmethod
    def _is_around_fifteen(cls, number):
         return number > (TEN + FIVE - 2)

    @classmethod
    def _is_around_ten(cls, number):
        return number > TEN - 2

    @classmethod
    def _is_around_five(cls, number):
         return number > (FIVE - 2)
