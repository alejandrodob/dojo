ONE = 'I'
FIVE = 'V'
TEN = 'X'

VALUE_FIVE = 5
VALUE_TEN = 10

class Roman(object):

    @classmethod
    def translate(cls, number):
        base_digit, base_digit_value = cls.base_roman_digit(number)
        remains_to_translate = number - base_digit_value
        if number <= 3:
            return cls.translate_lower_than_4(number)
        if base_digit_value - number == 1:
            return ONE + base_digit
        return base_digit + cls.translate(remains_to_translate)

    @classmethod
    def translate_lower_than_4(cls, number):
        return ONE * number

    @classmethod
    def base_roman_digit(cls, number):
        if number <= 3:
            return '', number
        if number - VALUE_TEN == -1 or VALUE_TEN - number <= 0:
            return TEN, VALUE_TEN
        if number - VALUE_FIVE == -1 or VALUE_FIVE - number <= 0:
            return FIVE, VALUE_FIVE
