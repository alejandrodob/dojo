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

    with it("translates 11 to XI"):
        expect(Roman.translate(11)).to(equal('XI'))

    with it("translates 12 to XII"):
        expect(Roman.translate(12)).to(equal('XII'))

    with it("translates 13 to XIII"):
        expect(Roman.translate(13)).to(equal('XIII'))

    with it("translates 14 to XIV"):
        expect(Roman.translate(14)).to(equal('XIV'))

    with it("translates 15 to XV"):
        expect(Roman.translate(15)).to(equal('XV'))

    with it("translates 16 to XVI"):
        expect(Roman.translate(16)).to(equal('XVI'))

    with it("translates 19 to XIX"):
        expect(Roman.translate(19)).to(equal('XIX'))

    with it("translates 20 to XX"):
        expect(Roman.translate(20)).to(equal('XX'))

    with it("translates 24 to XXIV"):
        expect(Roman.translate(24)).to(equal('XXIV'))

    with it("translates 39 to XXXIX"):
        expect(Roman.translate(39)).to(equal('XXXIX'))

    with it("translates 40 to XL"):
        expect(Roman.translate(40)).to(equal('XL'))

    with it("translates 44 to XLIV"):
        expect(Roman.translate(44)).to(equal('XLIV'))

    with it("translates 50 to L"):
        expect(Roman.translate(50)).to(equal('L'))

    with it("translates 89 to LXXXIX"):
        expect(Roman.translate(89)).to(equal('LXXXIX'))

    with it("translates 99 to XCIX"):
        expect(Roman.translate(99)).to(equal('XCIX'))

    with it("translates 100 to C"):
        expect(Roman.translate(100)).to(equal('C'))

    with it("translates 399 to CCCXCIX"):
        expect(Roman.translate(399)).to(equal('CCCXCIX'))