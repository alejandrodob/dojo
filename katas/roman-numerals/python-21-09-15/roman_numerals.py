ONE = 'I'
FIVE = 'V'
TEN = 'X'

VALUE_OF = {ONE: 1, FIVE: 5, TEN: 10}
SYMBOL_OF = {1: ONE, 5: FIVE, 10: TEN}


class Roman(object):

    @classmethod
    def translate(cls, number):
        base = cls.calculate_base_term(number)
        remain = (number - VALUE_OF[base])
        if number < 3:
            return cls.translate_three_or_below(number)
        if number == VALUE_OF[base] - 1:
            return ONE + base
        if number >= VALUE_OF[base]:
            return base + cls.translate(remain)


    @classmethod
    def translate_three_or_below(cls, number):
        return number * ONE

    @classmethod
    def calculate_base_term(cls, number):
        if number in VALUE_OF.values():
            return SYMBOL_OF[number]
        return max([key for key, value in VALUE_OF.items() if (number-value >= -1)])
