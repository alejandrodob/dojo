ROMAN_ONE = 'I'
ROMAN_FIVE = 'V'
ROMAN_TEN = 'X'

class Roman(object):

    @classmethod
    def translate(cls, number):
        if number > 8:
            return (10 - number) * ROMAN_ONE + ROMAN_TEN
        if number > 3:
            return (5 - number) * ROMAN_ONE + ROMAN_FIVE + (number - 5) * ROMAN_ONE
        return ROMAN_ONE * number
