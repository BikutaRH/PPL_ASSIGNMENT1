# Generated from d:\LEARNING\CQ_VB2\SEM_221\PPL\Ass_1\initial\assignment1\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u020a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\7\34\u0126")
        buf.write("\n\34\f\34\16\34\u0129\13\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\6\67\u0166\n\67")
        buf.write("\r\67\16\67\u0167\38\38\38\58\u016d\n8\38\58\u0170\n8")
        buf.write("\39\69\u0173\n9\r9\169\u0174\3:\3:\6:\u0179\n:\r:\16:")
        buf.write("\u017a\3;\3;\5;\u017f\n;\3;\6;\u0182\n;\r;\16;\u0183\3")
        buf.write("<\3<\5<\u0188\n<\3=\3=\7=\u018c\n=\f=\16=\u018f\13=\3")
        buf.write("=\3=\3=\3>\3>\5>\u0196\n>\3?\3?\3?\3@\3@\3@\3@\3A\3A\3")
        buf.write("A\3A\7A\u01a3\nA\fA\16A\u01a6\13A\3A\3A\3A\3A\7A\u01ac")
        buf.write("\nA\fA\16A\u01af\13A\3A\3A\3A\3A\7A\u01b5\nA\fA\16A\u01b8")
        buf.write("\13A\3A\3A\3A\3A\7A\u01be\nA\fA\16A\u01c1\13A\5A\u01c3")
        buf.write("\nA\3B\3B\7B\u01c7\nB\fB\16B\u01ca\13B\3B\3B\3B\3B\3C")
        buf.write("\3C\3C\3D\3D\3D\3E\3E\7E\u01d8\nE\fE\16E\u01db\13E\3E")
        buf.write("\3E\3F\6F\u01e0\nF\rF\16F\u01e1\3F\3F\3G\3G\7G\u01e8\n")
        buf.write("G\fG\16G\u01eb\13G\3G\5G\u01ee\nG\3G\3G\3H\3H\7H\u01f4")
        buf.write("\nH\fH\16H\u01f7\13H\3H\3H\3H\3I\3I\5I\u01fe\nI\3J\3J")
        buf.write("\3J\3K\3K\3K\5K\u0206\nK\3L\3L\3L\2\2M\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q\2s\2u\2w:y;{\2}\2\177")
        buf.write("<\u0081\2\u0083=\u0085\2\u0087\2\u0089>\u008b?\u008d@")
        buf.write("\u008fA\u0091\2\u0093\2\u0095\2\u0097B\3\2\17\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\4\2\f\f\17")
        buf.write("\17\t\2$$^^ddhhppttvv\6\2NOUUWWaa\5\2\13\f\16\17\"\"\7")
        buf.write("\3\n\f\16\17$$))^^\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhp")
        buf.write("pttvv\3\2^^\2\u0217\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0083\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2")
        buf.write("\2\5\u009b\3\2\2\2\7\u009e\3\2\2\2\t\u00a6\3\2\2\2\13")
        buf.write("\u00ac\3\2\2\2\r\u00b2\3\2\2\2\17\u00bb\3\2\2\2\21\u00be")
        buf.write("\3\2\2\2\23\u00c3\3\2\2\2\25\u00cb\3\2\2\2\27\u00d1\3")
        buf.write("\2\2\2\31\u00d4\3\2\2\2\33\u00d8\3\2\2\2\35\u00dc\3\2")
        buf.write("\2\2\37\u00e3\3\2\2\2!\u00e8\3\2\2\2#\u00ec\3\2\2\2%\u00f3")
        buf.write("\3\2\2\2\'\u00f8\3\2\2\2)\u00fe\3\2\2\2+\u0103\3\2\2\2")
        buf.write("-\u0107\3\2\2\2/\u010c\3\2\2\2\61\u0112\3\2\2\2\63\u0119")
        buf.write("\3\2\2\2\65\u011c\3\2\2\2\67\u0123\3\2\2\29\u012a\3\2")
        buf.write("\2\2;\u012c\3\2\2\2=\u012e\3\2\2\2?\u0130\3\2\2\2A\u0132")
        buf.write("\3\2\2\2C\u0134\3\2\2\2E\u0136\3\2\2\2G\u0139\3\2\2\2")
        buf.write("I\u013c\3\2\2\2K\u013e\3\2\2\2M\u0140\3\2\2\2O\u0143\3")
        buf.write("\2\2\2Q\u0146\3\2\2\2S\u0149\3\2\2\2U\u014c\3\2\2\2W\u014e")
        buf.write("\3\2\2\2Y\u0150\3\2\2\2[\u0152\3\2\2\2]\u0154\3\2\2\2")
        buf.write("_\u0156\3\2\2\2a\u0158\3\2\2\2c\u015a\3\2\2\2e\u015c\3")
        buf.write("\2\2\2g\u015e\3\2\2\2i\u0160\3\2\2\2k\u0162\3\2\2\2m\u0165")
        buf.write("\3\2\2\2o\u0169\3\2\2\2q\u0172\3\2\2\2s\u0176\3\2\2\2")
        buf.write("u\u017c\3\2\2\2w\u0187\3\2\2\2y\u0189\3\2\2\2{\u0195\3")
        buf.write("\2\2\2}\u0197\3\2\2\2\177\u019a\3\2\2\2\u0081\u01c2\3")
        buf.write("\2\2\2\u0083\u01c4\3\2\2\2\u0085\u01cf\3\2\2\2\u0087\u01d2")
        buf.write("\3\2\2\2\u0089\u01d5\3\2\2\2\u008b\u01df\3\2\2\2\u008d")
        buf.write("\u01e5\3\2\2\2\u008f\u01f1\3\2\2\2\u0091\u01fd\3\2\2\2")
        buf.write("\u0093\u01ff\3\2\2\2\u0095\u0205\3\2\2\2\u0097\u0207\3")
        buf.write("\2\2\2\u0099\u009a\7?\2\2\u009a\4\3\2\2\2\u009b\u009c")
        buf.write("\7<\2\2\u009c\u009d\7?\2\2\u009d\6\3\2\2\2\u009e\u009f")
        buf.write("\7d\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2")
        buf.write("\7n\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7p\2\2\u00a5\b\3\2\2\2\u00a6\u00a7\7d\2\2\u00a7\u00a8")
        buf.write("\7t\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab")
        buf.write("\7m\2\2\u00ab\n\3\2\2\2\u00ac\u00ad\7e\2\2\u00ad\u00ae")
        buf.write("\7n\2\2\u00ae\u00af\7c\2\2\u00af\u00b0\7u\2\2\u00b0\u00b1")
        buf.write("\7u\2\2\u00b1\f\3\2\2\2\u00b2\u00b3\7e\2\2\u00b3\u00b4")
        buf.write("\7q\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\16\3\2\2\2\u00bb\u00bc\7f\2\2\u00bc\u00bd")
        buf.write("\7q\2\2\u00bd\20\3\2\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0")
        buf.write("\7n\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2\7g\2\2\u00c2\22")
        buf.write("\3\2\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5\7z\2\2\u00c5\u00c6")
        buf.write("\7v\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7f\2\2\u00c9\u00ca\7u\2\2\u00ca\24\3\2\2\2\u00cb\u00cc")
        buf.write("\7h\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7c\2\2\u00cf\u00d0\7v\2\2\u00d0\26\3\2\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7h\2\2\u00d3\30\3\2\2\2\u00d4\u00d5")
        buf.write("\7k\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7\7v\2\2\u00d7\32")
        buf.write("\3\2\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7g\2\2\u00da\u00db")
        buf.write("\7y\2\2\u00db\34\3\2\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de")
        buf.write("\7v\2\2\u00de\u00df\7t\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1")
        buf.write("\7p\2\2\u00e1\u00e2\7i\2\2\u00e2\36\3\2\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4\u00e5\7j\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7 \3\2\2\2\u00e8\u00e9\7h\2\2\u00e9\u00ea")
        buf.write("\7q\2\2\u00ea\u00eb\7t\2\2\u00eb\"\3\2\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0")
        buf.write("\7w\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7p\2\2\u00f2$\3")
        buf.write("\2\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6")
        buf.write("\7w\2\2\u00f6\u00f7\7g\2\2\u00f7&\3\2\2\2\u00f8\u00f9")
        buf.write("\7h\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc")
        buf.write("\7u\2\2\u00fc\u00fd\7g\2\2\u00fd(\3\2\2\2\u00fe\u00ff")
        buf.write("\7x\2\2\u00ff\u0100\7q\2\2\u0100\u0101\7k\2\2\u0101\u0102")
        buf.write("\7f\2\2\u0102*\3\2\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7k\2\2\u0105\u0106\7n\2\2\u0106,\3\2\2\2\u0107\u0108")
        buf.write("\7v\2\2\u0108\u0109\7j\2\2\u0109\u010a\7k\2\2\u010a\u010b")
        buf.write("\7u\2\2\u010b.\3\2\2\2\u010c\u010d\7h\2\2\u010d\u010e")
        buf.write("\7k\2\2\u010e\u010f\7p\2\2\u010f\u0110\7c\2\2\u0110\u0111")
        buf.write("\7n\2\2\u0111\60\3\2\2\2\u0112\u0113\7u\2\2\u0113\u0114")
        buf.write("\7v\2\2\u0114\u0115\7c\2\2\u0115\u0116\7v\2\2\u0116\u0117")
        buf.write("\7k\2\2\u0117\u0118\7e\2\2\u0118\62\3\2\2\2\u0119\u011a")
        buf.write("\7v\2\2\u011a\u011b\7q\2\2\u011b\64\3\2\2\2\u011c\u011d")
        buf.write("\7f\2\2\u011d\u011e\7q\2\2\u011e\u011f\7y\2\2\u011f\u0120")
        buf.write("\7p\2\2\u0120\u0121\7v\2\2\u0121\u0122\7q\2\2\u0122\66")
        buf.write("\3\2\2\2\u0123\u0127\t\2\2\2\u0124\u0126\t\3\2\2\u0125")
        buf.write("\u0124\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u01288\3\2\2\2\u0129\u0127\3\2\2")
        buf.write("\2\u012a\u012b\7-\2\2\u012b:\3\2\2\2\u012c\u012d\7/\2")
        buf.write("\2\u012d<\3\2\2\2\u012e\u012f\7,\2\2\u012f>\3\2\2\2\u0130")
        buf.write("\u0131\7\61\2\2\u0131@\3\2\2\2\u0132\u0133\7^\2\2\u0133")
        buf.write("B\3\2\2\2\u0134\u0135\7\'\2\2\u0135D\3\2\2\2\u0136\u0137")
        buf.write("\7#\2\2\u0137\u0138\7?\2\2\u0138F\3\2\2\2\u0139\u013a")
        buf.write("\7?\2\2\u013a\u013b\7?\2\2\u013bH\3\2\2\2\u013c\u013d")
        buf.write("\7>\2\2\u013dJ\3\2\2\2\u013e\u013f\7@\2\2\u013fL\3\2\2")
        buf.write("\2\u0140\u0141\7>\2\2\u0141\u0142\7?\2\2\u0142N\3\2\2")
        buf.write("\2\u0143\u0144\7@\2\2\u0144\u0145\7?\2\2\u0145P\3\2\2")
        buf.write("\2\u0146\u0147\7~\2\2\u0147\u0148\7~\2\2\u0148R\3\2\2")
        buf.write("\2\u0149\u014a\7(\2\2\u014a\u014b\7(\2\2\u014bT\3\2\2")
        buf.write("\2\u014c\u014d\7#\2\2\u014dV\3\2\2\2\u014e\u014f\7`\2")
        buf.write("\2\u014fX\3\2\2\2\u0150\u0151\7]\2\2\u0151Z\3\2\2\2\u0152")
        buf.write("\u0153\7_\2\2\u0153\\\3\2\2\2\u0154\u0155\7}\2\2\u0155")
        buf.write("^\3\2\2\2\u0156\u0157\7\177\2\2\u0157`\3\2\2\2\u0158\u0159")
        buf.write("\7*\2\2\u0159b\3\2\2\2\u015a\u015b\7+\2\2\u015bd\3\2\2")
        buf.write("\2\u015c\u015d\7=\2\2\u015df\3\2\2\2\u015e\u015f\7<\2")
        buf.write("\2\u015fh\3\2\2\2\u0160\u0161\7\60\2\2\u0161j\3\2\2\2")
        buf.write("\u0162\u0163\7.\2\2\u0163l\3\2\2\2\u0164\u0166\t\4\2\2")
        buf.write("\u0165\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0165\3")
        buf.write("\2\2\2\u0167\u0168\3\2\2\2\u0168n\3\2\2\2\u0169\u016f")
        buf.write("\5q9\2\u016a\u016c\5s:\2\u016b\u016d\5u;\2\u016c\u016b")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u0170\3\2\2\2\u016e")
        buf.write("\u0170\5u;\2\u016f\u016a\3\2\2\2\u016f\u016e\3\2\2\2\u0170")
        buf.write("p\3\2\2\2\u0171\u0173\t\4\2\2\u0172\u0171\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175r\3\2\2\2\u0176\u0178\7\60\2\2\u0177\u0179\t\4\2")
        buf.write("\2\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0178")
        buf.write("\3\2\2\2\u017a\u017b\3\2\2\2\u017bt\3\2\2\2\u017c\u017e")
        buf.write("\t\5\2\2\u017d\u017f\t\6\2\2\u017e\u017d\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u0181\3\2\2\2\u0180\u0182\t\4\2\2")
        buf.write("\u0181\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0181\3")
        buf.write("\2\2\2\u0183\u0184\3\2\2\2\u0184v\3\2\2\2\u0185\u0188")
        buf.write("\5%\23\2\u0186\u0188\5\'\24\2\u0187\u0185\3\2\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188x\3\2\2\2\u0189\u018d\7$\2\2\u018a")
        buf.write("\u018c\5{>\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0190\3\2\2\2")
        buf.write("\u018f\u018d\3\2\2\2\u0190\u0191\7$\2\2\u0191\u0192\b")
        buf.write("=\2\2\u0192z\3\2\2\2\u0193\u0196\n\7\2\2\u0194\u0196\5")
        buf.write("}?\2\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2\u0196|\3")
        buf.write("\2\2\2\u0197\u0198\7^\2\2\u0198\u0199\t\b\2\2\u0199~\3")
        buf.write("\2\2\2\u019a\u019b\5]/\2\u019b\u019c\5\u0081A\2\u019c")
        buf.write("\u019d\5_\60\2\u019d\u0080\3\2\2\2\u019e\u01a4\5m\67\2")
        buf.write("\u019f\u01a0\5k\66\2\u01a0\u01a1\5m\67\2\u01a1\u01a3\3")
        buf.write("\2\2\2\u01a2\u019f\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2")
        buf.write("\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01c3\3\2\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a7\u01ad\5o8\2\u01a8\u01a9\5k\66\2\u01a9")
        buf.write("\u01aa\5o8\2\u01aa\u01ac\3\2\2\2\u01ab\u01a8\3\2\2\2\u01ac")
        buf.write("\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01ae\u01c3\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b6\5")
        buf.write("w<\2\u01b1\u01b2\5k\66\2\u01b2\u01b3\5w<\2\u01b3\u01b5")
        buf.write("\3\2\2\2\u01b4\u01b1\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01c3\3\2\2\2")
        buf.write("\u01b8\u01b6\3\2\2\2\u01b9\u01bf\5y=\2\u01ba\u01bb\5k")
        buf.write("\66\2\u01bb\u01bc\5y=\2\u01bc\u01be\3\2\2\2\u01bd\u01ba")
        buf.write("\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf")
        buf.write("\u01c0\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2")
        buf.write("\u01c2\u019e\3\2\2\2\u01c2\u01a7\3\2\2\2\u01c2\u01b0\3")
        buf.write("\2\2\2\u01c2\u01b9\3\2\2\2\u01c3\u0082\3\2\2\2\u01c4\u01c8")
        buf.write("\5\u0085C\2\u01c5\u01c7\n\t\2\2\u01c6\u01c5\3\2\2\2\u01c7")
        buf.write("\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9\u01cb\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\5")
        buf.write("\u0087D\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\bB\3\2\u01ce")
        buf.write("\u0084\3\2\2\2\u01cf\u01d0\7\61\2\2\u01d0\u01d1\7,\2\2")
        buf.write("\u01d1\u0086\3\2\2\2\u01d2\u01d3\7,\2\2\u01d3\u01d4\7")
        buf.write("\61\2\2\u01d4\u0088\3\2\2\2\u01d5\u01d9\7%\2\2\u01d6\u01d8")
        buf.write("\n\7\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9")
        buf.write("\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2")
        buf.write("\u01db\u01d9\3\2\2\2\u01dc\u01dd\bE\3\2\u01dd\u008a\3")
        buf.write("\2\2\2\u01de\u01e0\t\n\2\2\u01df\u01de\3\2\2\2\u01e0\u01e1")
        buf.write("\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2")
        buf.write("\u01e3\3\2\2\2\u01e3\u01e4\bF\3\2\u01e4\u008c\3\2\2\2")
        buf.write("\u01e5\u01e9\7$\2\2\u01e6\u01e8\5\u0091I\2\u01e7\u01e6")
        buf.write("\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2\u01e9")
        buf.write("\u01ea\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9\3\2\2\2")
        buf.write("\u01ec\u01ee\t\13\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01ef")
        buf.write("\3\2\2\2\u01ef\u01f0\bG\4\2\u01f0\u008e\3\2\2\2\u01f1")
        buf.write("\u01f5\7$\2\2\u01f2\u01f4\5\u0091I\2\u01f3\u01f2\3\2\2")
        buf.write("\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6")
        buf.write("\3\2\2\2\u01f6\u01f8\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8")
        buf.write("\u01f9\5\u0095K\2\u01f9\u01fa\bH\5\2\u01fa\u0090\3\2\2")
        buf.write("\2\u01fb\u01fe\n\f\2\2\u01fc\u01fe\5\u0093J\2\u01fd\u01fb")
        buf.write("\3\2\2\2\u01fd\u01fc\3\2\2\2\u01fe\u0092\3\2\2\2\u01ff")
        buf.write("\u0200\7^\2\2\u0200\u0201\t\r\2\2\u0201\u0094\3\2\2\2")
        buf.write("\u0202\u0203\7^\2\2\u0203\u0206\n\r\2\2\u0204\u0206\n")
        buf.write("\16\2\2\u0205\u0202\3\2\2\2\u0205\u0204\3\2\2\2\u0206")
        buf.write("\u0096\3\2\2\2\u0207\u0208\13\2\2\2\u0208\u0209\bL\6\2")
        buf.write("\u0209\u0098\3\2\2\2\33\2\u0127\u0167\u016c\u016f\u0174")
        buf.write("\u017a\u017e\u0183\u0187\u018d\u0195\u01a4\u01ad\u01b6")
        buf.write("\u01bf\u01c2\u01c8\u01d9\u01e1\u01e9\u01ed\u01f5\u01fd")
        buf.write("\u0205\7\3=\2\b\2\2\3G\3\3H\4\3L\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EQ = 1
    ASSIGN = 2
    BOOLEAN = 3
    BREAK = 4
    CLASS = 5
    CONTINUE = 6
    DO = 7
    ELSE = 8
    EXTENDS = 9
    FLOAT = 10
    IF = 11
    INT = 12
    NEW = 13
    STRING = 14
    THEN = 15
    FOR = 16
    RETURN = 17
    TRUE = 18
    FALSE = 19
    VOID = 20
    NIL = 21
    THIS = 22
    FINAL = 23
    STATIC = 24
    TO = 25
    DOWNTO = 26
    ID = 27
    ADD = 28
    SUB = 29
    MUL = 30
    FLDIV = 31
    INDIV = 32
    MOD = 33
    NOTEQUAL = 34
    EQUAL = 35
    LESS = 36
    GREATER = 37
    LQ = 38
    GQ = 39
    OR = 40
    AND = 41
    NOT = 42
    CONCA = 43
    LSB = 44
    RSB = 45
    LP = 46
    RP = 47
    LB = 48
    RB = 49
    SEMI = 50
    COLON = 51
    DOT = 52
    COMMA = 53
    INTLIT = 54
    FLOATLIT = 55
    BOOLIT = 56
    STRINGLIT = 57
    ARRLIT = 58
    BLOCK_COMMENT = 59
    LINE_COMMENT = 60
    WS = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "':='", "'boolean'", "'break'", "'class'", "'continue'", 
            "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", "'new'", 
            "'string'", "'then'", "'for'", "'return'", "'true'", "'false'", 
            "'void'", "'nil'", "'this'", "'final'", "'static'", "'to'", 
            "'downto'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
            "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", 
            "'^'", "'['", "']'", "'{'", "'}'", "'('", "')'", "';'", "':'", 
            "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "EQ", "ASSIGN", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", 
            "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", 
            "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", 
            "STATIC", "TO", "DOWNTO", "ID", "ADD", "SUB", "MUL", "FLDIV", 
            "INDIV", "MOD", "NOTEQUAL", "EQUAL", "LESS", "GREATER", "LQ", 
            "GQ", "OR", "AND", "NOT", "CONCA", "LSB", "RSB", "LP", "RP", 
            "LB", "RB", "SEMI", "COLON", "DOT", "COMMA", "INTLIT", "FLOATLIT", 
            "BOOLIT", "STRINGLIT", "ARRLIT", "BLOCK_COMMENT", "LINE_COMMENT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "EQ", "ASSIGN", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                  "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
                  "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", 
                  "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", "ID", 
                  "ADD", "SUB", "MUL", "FLDIV", "INDIV", "MOD", "NOTEQUAL", 
                  "EQUAL", "LESS", "GREATER", "LQ", "GQ", "OR", "AND", "NOT", 
                  "CONCA", "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI", 
                  "COLON", "DOT", "COMMA", "INTLIT", "FLOATLIT", "INTPART", 
                  "FRACPART", "EXPART", "BOOLIT", "STRINGLIT", "CHARACTERS", 
                  "ESCAPE", "ARRLIT", "NONNULL_LIT", "BLOCK_COMMENT", "SL_MU", 
                  "MU_SL", "LINE_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.STRINGLIT_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise ErrorToken(self.text)
            	
     


