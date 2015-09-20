from roman_numerals import Roman
from expects import *


with describe(Roman):
    with it("translates 1 to I"):
        expect(Roman.translate(1)).to(equal('I'))

    with it("translates 2 to II"):
        expect(Roman.translate(2)).to(equal('II'))

    with it("translates 3 to III"):
        expect(Roman.translate(3)).to(equal('III'))

    with it("translates 4 to IV"):
        expect(Roman.translate(4)).to(equal('IV'))

    with it("translates 5 to V"):
        expect(Roman.translate(5)).to(equal('V'))