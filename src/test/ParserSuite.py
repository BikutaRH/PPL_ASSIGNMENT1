import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    
    def test_1(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_2(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_3(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_4(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))
       
    def test_5(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_6(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_7(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_8(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_9(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_10(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_11(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_12(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_13(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_14(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_15(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_16(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_17(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_18(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_19(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_20(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_21(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_22(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))
       
    def test_23(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_24(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_25(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_26(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_27(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_28(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_29(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_30(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_31(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_32(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_33(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_34(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_35(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_36(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_37(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_38(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_39(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_40(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))
       
    def test_41(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_42(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_43(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_44(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_45(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_46(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_47(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_48(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_49(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_50(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_51(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_52(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_53(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_54(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_55(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_56(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_57(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_58(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))
       
    def test_59(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_60(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_61(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_62(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_63(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_64(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_65(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_66(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_67(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_68(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_69(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_70(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_71(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_72(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_73(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_74(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_75(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_76(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))
       
    def test_77(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_78(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_79(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_80(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_81(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_82(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_83(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_84(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_85(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_86(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_87(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_88(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_89(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_90(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_91(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_92(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_93(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_94(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))
       
    def test_95(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_96(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_97(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_98(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_99(self):
        """Simple program: int main() {} """
        input = """class ABC { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_100(self):
        """More complex program"""
        input = """class ABC extends { }"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))

