ONE = 'I'
FIVE = 'V'

class Roman(object):

    @classmethod
    def translate(cls, number):
        if number == 5:
            return FIVE
        if number >= 4:
            return ONE + FIVE
        return number * ONE
