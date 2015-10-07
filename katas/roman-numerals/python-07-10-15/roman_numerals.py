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
    interval = range(value, value + TEN.value)

class NINETY(object):
    symbol = TEN. symbol + HUNDRED.symbol
    value = HUNDRED.value - TEN.value
    interval = range(value, value + TEN.value)


class Roman(object):

    @staticmethod
    def translate(number):

        if number <= 3:
            return ONE.symbol * number

        base = Roman.base_roman_for(number)
        return base.symbol + Roman.translate(number - base.value)

    @staticmethod
    def is_special_value(number):
        return number in [FOUR.value, NINE.value] + FOURTY.interval + NINETY.interval

    @staticmethod
    def base_roman_for(number):

        if number in NINETY.interval:
            return NINETY
        if number in FOURTY.interval:
            return FOURTY
        if number == FOUR.value:
            return FOUR
        if number == NINE.value:
            return NINE

        if number >= HUNDRED.value:
            return HUNDRED
        if number >= FIFTY.value:
            return FIFTY
        if number >= TEN.value:
            return TEN
        if number >= FIVE.value:
            return FIVE
