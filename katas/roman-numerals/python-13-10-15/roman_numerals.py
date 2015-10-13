class ONE(object):
    roman = 'I'
    value = 1
    left_allowed = None

    @staticmethod
    def roman_for(number):
        return ONE.roman

    @staticmethod
    def interval():
        return range(4)

    @staticmethod
    def remaining_for(number):
        return number - ONE.value

class FIVE(object):
    roman = 'V'
    value = 5
    left_allowed = ONE

    @staticmethod
    def roman_for(number):
        if number < FIVE.value:
            return FIVE.left_allowed.roman + FIVE.roman
        return FIVE.roman

    @staticmethod
    def interval():
        return range(4, 9)

    @staticmethod
    def remaining_for(number):
        if number < FIVE.value:
            return 0
        return number - FIVE.value

class TEN(object):
    roman = 'X'
    value = 10
    left_allowed = ONE

    @staticmethod
    def roman_for(number):
        if number < TEN.value:
            return TEN.left_allowed.roman + TEN.roman
        return TEN.roman

    @staticmethod
    def interval():
        return range(9, 40)

    @staticmethod
    def remaining_for(number):
        if number < TEN.value:
            return 0
        return number - TEN.value

class FIFTY(object):
    roman = 'L'
    value = 50
    left_allowed = TEN

    @staticmethod
    def roman_for(number):
        if number < FIFTY.value:
            return FIFTY.left_allowed.roman + FIFTY.roman
        return FIFTY.roman

    @staticmethod
    def interval():
        return range(40, 90)

    @staticmethod
    def remaining_for(number):
        if number < FIFTY.value:
            return number - (FIFTY.value - FIFTY.left_allowed.value)
        return number - FIFTY.value

all_romans = [FIVE, TEN, FIFTY]


class Roman(object):

    @staticmethod
    def translate(number):
        closest_roman_symbol = Roman.find_closest_roman_to(number)
        base_symbol = closest_roman_symbol.roman_for(number)
        remaining = closest_roman_symbol.remaining_for(number)
        remaining_roman = Roman.translate(remaining) if base_symbol != ONE and remaining > 0 else ''

        return base_symbol + remaining_roman

    @staticmethod
    def find_closest_roman_to(number):
        found_roman = ONE
        for roman in all_romans:
            if number in roman.interval():
                return roman
        return found_roman

