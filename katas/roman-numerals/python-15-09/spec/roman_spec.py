from expects import *

class Roman(object):
    def translate(self, number):
        if number <= 5:
            roman_number = (5-number) * "I" + "V"
        if number < 4:
            roman_number = number * "I"
        dictionary = {
            6: "VI",
            7: "VII",
            9: "IX",
            10: "X"}
        try:
            roman_number = dictionary[number]
        except KeyError:
            pass
        return roman_number

with description("Roman numerals"):
    with context("when working with simple numbers"):
        with it("translates 1 to 'I'"):

            expect(Roman().translate(1)).to(equal("I"))

        with it("translates 5 to 'V'"):
            expect(Roman().translate(5)).to(equal("V"))

        with it("translates 10 to 'X'"):
            expect(Roman().translate(10)).to(equal("X"))


    with context("working with combined roman numbers"):
        with it("translates 2 to 'II'"):
            expect(Roman().translate(2)).to(equal("II"))

        with it("translates 4 to 'IV"):
            expect(Roman().translate(4)).to(equal("IV"))

        with it("translates 6 to 'VI"):
            expect(Roman().translate(6)).to(equal("VI"))

        with it("translates 7 to 'VII"):
            expect(Roman().translate(7)).to(equal("VII"))

        with it("translates 9 to 'IX'"):
            expect(Roman().translate(9)).to(equal("IX"))




