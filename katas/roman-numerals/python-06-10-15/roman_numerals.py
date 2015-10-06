ONE = 'I'
FIVE = 'V'
TEN = 'X'
FIFTY = 'L'
HUNDRED = 'C'

VALUE_ONE = 1
VALUE_FIVE = 5
VALUE_TEN = 10
VALUE_FIFTY = 50
VALUE_HUNDRED = 100

class Roman(object):

    @staticmethod
    def translate(number):

        if number/VALUE_TEN == VALUE_TEN - VALUE_ONE:
            return TEN + HUNDRED + Roman.translate(number - (VALUE_HUNDRED - VALUE_TEN))
        if number/VALUE_TEN == VALUE_FIVE - VALUE_ONE:
            return TEN + FIFTY + Roman.translate(number - (VALUE_FIFTY - VALUE_TEN))
        if number == VALUE_TEN - VALUE_ONE:
            return ONE + TEN
        if number == VALUE_FIVE - VALUE_ONE:
            return ONE + FIVE

        if number >= VALUE_HUNDRED:
            return HUNDRED + Roman.translate(number - VALUE_HUNDRED)
        if number >= VALUE_FIFTY:
            return FIFTY + Roman.translate(number - VALUE_FIFTY)
        if number >= VALUE_TEN:
            return TEN + Roman.translate(number - VALUE_TEN)
        if number >= VALUE_FIVE:
            return FIVE + Roman.translate(number - VALUE_FIVE)

        return number * ONE
