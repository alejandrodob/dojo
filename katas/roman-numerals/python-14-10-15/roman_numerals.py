class UnitsTranslator(object):
    UNIT = 'I'
    QUINTET = 'V'
    QUINTET_FACTOR = 5
    SPECIAL_CASES = {4: 'IV', 9: 'IX'}

    def express(self, value):
        if self.is_special_case(value):
            return self.express_special_case(value)

        return self.express_regular_case(value)

    def express_in_units(self, value=0):
        return self.UNIT * value

    def express_in_quintets(self, value=0):
        if value < self.QUINTET_FACTOR:
            return ''
        return self.QUINTET

    def is_special_case(self, value):
        return value in self.SPECIAL_CASES

    def express_special_case(self, value):
        return self.SPECIAL_CASES[value]

    def calculate_remaining(self, quintets, value):
        remaining = value
        if quintets != '':
            remaining = value - self.QUINTET_FACTOR
        return remaining

    def express_regular_case(self, value):
        quintets = self.express_in_quintets(value)

        remaining = self.calculate_remaining(quintets, value)

        symbol = quintets + self.express_in_units(remaining)
        return symbol

class TensTranslator(object):
    UNIT = 'X'
    QUINTET = 'L'
    QUINTET_FACTOR = 5
    SPECIAL_CASES = {4: 'XL', 9: 'XC'}

    def express(self, value):
        if self.is_special_case(value):
            return self.express_special_case(value)

        return self.express_regular_case(value)

    def express_in_units(self, value=0):
        return self.UNIT * value

    def express_in_quintets(self, value=0):
        if value < self.QUINTET_FACTOR:
            return ''
        return self.QUINTET

    def is_special_case(self, value):
        return value in self.SPECIAL_CASES

    def express_special_case(self, value):
        return self.SPECIAL_CASES[value]

    def calculate_remaining(self, quintets, value):
        remaining = value
        if quintets != '':
            remaining = value - self.QUINTET_FACTOR
        return remaining

    def express_regular_case(self, value):
        quintets = self.express_in_quintets(value)

        remaining = self.calculate_remaining(quintets, value)

        symbol = quintets + self.express_in_units(remaining)
        return symbol



class RomanNumeral(object):

    def __init__(self, number):
        self.value = number
        self.units_translator = UnitsTranslator()
        self.tens_translator = TensTranslator()

    def express(self):
        units = self.value % 10
        tens = self.value / 10
        return self.tens_translator.express(tens) + self.units_translator.express(units)



class Roman(object):

    @staticmethod
    def translate(number):
        return RomanNumeral(number).express()
