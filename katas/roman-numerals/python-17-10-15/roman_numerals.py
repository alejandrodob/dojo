class Translator(object):
    QUINTET_VALUE = 5

    def __init__(self, unit, quintet, special_cases):
        self.unit = unit
        self.quintet = quintet
        self.special_cases = special_cases

    def express(self):
        if self.is_special_case():
            return self.express_special_case()

        return self.express_regular_case()

    def is_special_case(self):
        return self.value in self.special_cases

    def express_special_case(self):
        return self.special_cases[self.value]

    def express_regular_case(self):
        quintets = self.express_quintets(self.value)
        remaining = self.calculate_remaining(quintets)
        units = self.express_units(remaining)
        return quintets + units

    def express_units(self, number):
        return self.unit * number

    def express_quintets(self, number):
        if number < self.QUINTET_VALUE:
            return ''
        return self.quintet

    def calculate_remaining(self, quintets):
        if quintets:
            return self.value - self.QUINTET_VALUE
        return self.value

class UnitTranslator(Translator):
    UNIT = 'I'
    QUINTET = 'V'
    SPECIAL_CASES = {4: 'IV', 9: 'IX'}

    def __init__(self, number):
        super(UnitTranslator, self).__init__(self.UNIT, self.QUINTET, self.SPECIAL_CASES)
        self.value = number


class TensTranslator(Translator):
    UNIT = 'X'
    QUINTET = 'L'
    SPECIAL_CASES = {4: 'XL', 9: 'XC'}

    def __init__(self, number):
        super(TensTranslator, self).__init__(self.UNIT, self.QUINTET, self.SPECIAL_CASES)
        self.value = number


class HundredsTranslator(Translator):
    UNIT = 'C'
    QUINTET = 'D'
    SPECIAL_CASES = {4: 'CD', 9: 'CM'}

    def __init__(self, number):
        super(HundredsTranslator, self).__init__(self.UNIT, self.QUINTET, self.SPECIAL_CASES)
        self.value = number


class RomanNumeral(object):

    def __init__(self, number):
        self.value = number

    def express(self):
        hundreds = self.value / 100
        units = (self.value - hundreds * 100) % 10
        tens = (self.value - hundreds * 100) / 10
        units_representation = UnitTranslator(units).express()
        tens_representation = TensTranslator(tens).express()
        hundreds_representation = HundredsTranslator(hundreds).express()

        return hundreds_representation + tens_representation + units_representation


class Roman(object):

    @staticmethod
    def translate(number):
        return RomanNumeral(number).express()
