ROMAN_ONE = 'I'
ROMAN_FIVE = 'V'

class Roman(object):

    @classmethod
    def translate(cls, number):
        if number > 3:
            return (5 - number) * ROMAN_ONE + ROMAN_FIVE + (number - 5) * ROMAN_ONE
        return ROMAN_ONE * number
