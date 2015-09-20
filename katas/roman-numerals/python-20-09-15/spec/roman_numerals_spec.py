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

    with it("translates 6 to VI"):
        expect(Roman.translate(6)).to(equal('VI'))

    with it("translates 7 to VII"):
        expect(Roman.translate(7)).to(equal('VII'))

    with it("translates 8 to VIII"):
        expect(Roman.translate(8)).to(equal('VIII'))

    with it("translates 9 to IX"):
        expect(Roman.translate(9)).to(equal('IX'))

    with it("translates 10 to X"):
        expect(Roman.translate(10)).to(equal('X'))

