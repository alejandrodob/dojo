class Units(object):
    UNIT = 'I'
    QUINTET = 'V'
    QUINTET_VALUE = 5
    SPECIAL_CASES = {4: 'IV', 9: 'IX'}

    def __init__(self, number):
        self.value = number

    def engrave(self):
        if self._is_special_case():
            return self._engrave_special_case()
        return self._engrave_quintets() + self._engrave_units()

    def _engrave_quintets(self):
        if self.value < self.QUINTET_VALUE:
            return ''
        return self.QUINTET

    def _engrave_units(self):
        if self.value < self.QUINTET_VALUE:
            return self.UNIT * self.value
        return self.UNIT * (self.value - self.QUINTET_VALUE)

    def _is_special_case(self):
        return self.value in self.SPECIAL_CASES

    def _engrave_special_case(self):
        return self.SPECIAL_CASES[self.value]

class Tens(object):
    UNIT = 'X'
    QUINTET = 'L'
    QUINTET_VALUE = 5
    SPECIAL_CASES = {4: 'XL', 9: 'XC'}

    def __init__(self, number):
        self.value = number

    def engrave(self):
        if self._is_special_case():
            return self._engrave_special_case()
        return self._engrave_quintets() + self._engrave_units()

    def _engrave_quintets(self):
        if self.value < self.QUINTET_VALUE:
            return ''
        return self.QUINTET

    def _engrave_units(self):
        if self.value < self.QUINTET_VALUE:
            return self.UNIT * self.value
        return self.UNIT * (self.value - self.QUINTET_VALUE)

    def _is_special_case(self):
        return self.value in self.SPECIAL_CASES

    def _engrave_special_case(self):
        return self.SPECIAL_CASES[self.value]

class Hundreds(object):
    UNIT = 'C'
    QUINTET = 'D'
    QUINTET_VALUE = 5
    SPECIAL_CASES = {4: 'CD', 9: 'CM'}

    def __init__(self, number):
        self.value = number

    def engrave(self):
        if self._is_special_case():
            return self._engrave_special_case()
        return self._engrave_quintets() + self._engrave_units()

    def _engrave_quintets(self):
        if self.value < self.QUINTET_VALUE:
            return ''
        return self.QUINTET

    def _engrave_units(self):
        if self.value < self.QUINTET_VALUE:
            return self.UNIT * self.value
        return self.UNIT * (self.value - self.QUINTET_VALUE)

    def _is_special_case(self):
        return self.value in self.SPECIAL_CASES

    def _engrave_special_case(self):
        return self.SPECIAL_CASES[self.value]


class Numeral(object):

    def __init__(self, number):
        self.value = number

    def engrave(self):
        hundreds = self._engrave_hundreds()
        tens = self._engrave_tens()
        units = self._engrave_units()
        return hundreds + tens + units

    def _engrave_hundreds(self):
        amount_of_hundreds = self.value / 100
        return Hundreds(amount_of_hundreds).engrave()

    def _engrave_tens(self):
        remaining = self.value % 100
        amount_of_tens = remaining / 10
        return Tens(amount_of_tens).engrave()

    def _engrave_units(self):
        remaining = (self.value % 100) % 10
        return Units(remaining).engrave()

class Roman(object):

    @staticmethod
    def translate(number):
        return Numeral(number).engrave()
