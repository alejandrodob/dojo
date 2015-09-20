ROMAN_ONE = 'I'
ROMAN_FIVE = 'V'
ROMAN_TEN = 'X'

FIVE = 5
TEN = 10

VALUES = {'I': 1, 'V': 5, 'X': 10}

class Roman(object):

    @classmethod
    def translate(cls, number):
        if number <= 3:
            return ROMAN_ONE * number

        left_part = cls._biggest_roman_symbol_in(number)
        left_part_value = cls._value_for_roman(left_part)
        return left_part + cls._direct_translation_for(number-left_part_value)

    @classmethod
    def _direct_translation_for(cls, number):
        if cls._is_around_ten(number):
            return (TEN - number) * ROMAN_ONE + ROMAN_TEN
        if cls._is_around_five(number):
            return (FIVE - number) * ROMAN_ONE + ROMAN_FIVE



    @classmethod
    def _biggest_roman_symbol_in(cls, number):
        if number >= TEN:
            return ROMAN_TEN
        if number >= FIVE:
            return ROMAN_FIVE
        return ROMAN_ONE

    @classmethod
    def _value_for_roman(cls, roman_symbol):
        return VALUES[roman_symbol]

    @classmethod
    def _is_around_fifteen(cls, number):
         return number > (TEN + FIVE - 2)

    @classmethod
    def _is_around_ten(cls, number):
        return number > TEN - 2

    @classmethod
    def _is_around_five(cls, number):
         return number > (FIVE - 2)
