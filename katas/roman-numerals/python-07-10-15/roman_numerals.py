class ONE(object):
    symbol = 'I'
    value = 1

class FIVE(object):
    symbol = 'V'
    value = 5

class TEN(object):
    symbol = 'X'
    value = 10

class FIFTY(object):
    symbol = 'L'
    value = 50

class HUNDRED(object):
    symbol = 'C'
    value = 100

class FOUR(object):
    symbol = ONE.symbol + FIVE.symbol
    value = FIVE.value - ONE.value

class NINE(object):
    symbol = ONE.symbol + TEN.symbol
    value = TEN.value - ONE.value

class FOURTY(object):
    symbol = TEN.symbol + FIFTY.symbol
    value = FIFTY.value - TEN.value

class NINETY(object):
    symbol = TEN. symbol + HUNDRED.symbol
    value = HUNDRED.value - TEN.value


class Roman(object):

    @staticmethod
    def translate(number):

        if NINETY.value <= number < HUNDRED.value:
            return NINETY.symbol + Roman.translate(number - NINETY.value)
        if FOURTY.value <= number < FIFTY.value:
            return FOURTY.symbol + Roman.translate(number - FOURTY.value)
        if number == FOUR.value:
            return FOUR.symbol
        if number == NINE.value:
            return NINE.symbol


        if number >= HUNDRED.value:
            return HUNDRED.symbol + Roman.translate(number - HUNDRED.value)
        if number >= FIFTY.value:
            return FIFTY.symbol + Roman.translate(number - FIFTY.value)
        if number >= TEN.value:
            return TEN.symbol + Roman.translate(number - TEN.value)
        if number >= FIVE.value:
            return FIVE.symbol + Roman.translate(number - FIVE.value)

        return ONE.symbol * number
