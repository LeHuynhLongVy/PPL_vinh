# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u027a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\3\2\6\2\u0090\n\2\r\2\16\2\u0091\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\5\3\u009a\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\5\4\u00a4\n\4\3\5\3\5\3\5\3\5\5\5\u00aa")
        buf.write("\n\5\3\6\3\6\5\6\u00ae\n\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write("\u00b6\n\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u00c2\n\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u00d0\n\f\3\r\3\r\3\r\3\r\5\r\u00d6\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00dd\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u00ea\n\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u0106\n\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32")
        buf.write("\u0115\n\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u011d\n")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\5\35")
        buf.write("\u0128\n\35\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \5 \u0137\n \3!\3!\3!\3!\5!\u013d\n!\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\5%\u0151\n")
        buf.write("%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\7\'\u0164\n\'\f\'\16\'\u0167\13\'\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\7")
        buf.write("(\u017e\n(\f(\16(\u0181\13(\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\7)\u018c\n)\f)\16)\u018f\13)\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\7*\u019a\n*\f*\16*\u019d\13*\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3+\3+\7+\u01ab\n+\f+\16+\u01ae\13+\3,\3,\3")
        buf.write(",\5,\u01b3\n,\3-\3-\3-\5-\u01b8\n-\3.\3.\3.\3.\3.\7.\u01bf")
        buf.write("\n.\f.\16.\u01c2\13.\3/\3/\3/\3/\3/\3/\3/\7/\u01cb\n/")
        buf.write("\f/\16/\u01ce\13/\3\60\3\60\3\60\5\60\u01d3\n\60\3\61")
        buf.write("\3\61\5\61\u01d7\n\61\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\5\62\u01e4\n\62\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\5\64\u01f4\n\64\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u01fc")
        buf.write("\n\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\5\67\u0208\n\67\38\38\39\39\39\39\39\39\59\u0212\n9\3")
        buf.write("9\39\3:\3:\3:\3;\3;\3;\3;\3;\5;\u021e\n;\3<\3<\3=\3=\3")
        buf.write("=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u0232\n>\3")
        buf.write("?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\7?\u023f\n?\f?\16?\u0242")
        buf.write("\13?\3?\3?\5?\u0246\n?\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u0251")
        buf.write("\n@\3@\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\5C\u025e\nC\3C\3")
        buf.write("C\3D\3D\3D\3D\5D\u0266\nD\3D\3D\3E\3E\3E\3E\3F\3F\3F\3")
        buf.write("F\5F\u0272\nF\3G\3G\3G\3G\5G\u0278\nG\3G\2\tLNPRTZ\\H")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\2\4\3\2\31\32\3\2<=\2\u0286")
        buf.write("\2\u008f\3\2\2\2\4\u0095\3\2\2\2\6\u00a3\3\2\2\2\b\u00a9")
        buf.write("\3\2\2\2\n\u00ad\3\2\2\2\f\u00af\3\2\2\2\16\u00b9\3\2")
        buf.write("\2\2\20\u00c1\3\2\2\2\22\u00c3\3\2\2\2\24\u00c5\3\2\2")
        buf.write("\2\26\u00cf\3\2\2\2\30\u00d5\3\2\2\2\32\u00dc\3\2\2\2")
        buf.write("\34\u00de\3\2\2\2\36\u00e2\3\2\2\2 \u00e9\3\2\2\2\"\u00eb")
        buf.write("\3\2\2\2$\u00ed\3\2\2\2&\u00f3\3\2\2\2(\u00f8\3\2\2\2")
        buf.write("*\u00fd\3\2\2\2,\u0105\3\2\2\2.\u0107\3\2\2\2\60\u010c")
        buf.write("\3\2\2\2\62\u0114\3\2\2\2\64\u011c\3\2\2\2\66\u011e\3")
        buf.write("\2\2\28\u0127\3\2\2\2:\u0129\3\2\2\2<\u012b\3\2\2\2>\u0136")
        buf.write("\3\2\2\2@\u013c\3\2\2\2B\u013e\3\2\2\2D\u0141\3\2\2\2")
        buf.write("F\u0145\3\2\2\2H\u014b\3\2\2\2J\u0154\3\2\2\2L\u015a\3")
        buf.write("\2\2\2N\u0168\3\2\2\2P\u0182\3\2\2\2R\u0190\3\2\2\2T\u019e")
        buf.write("\3\2\2\2V\u01b2\3\2\2\2X\u01b7\3\2\2\2Z\u01b9\3\2\2\2")
        buf.write("\\\u01c3\3\2\2\2^\u01d2\3\2\2\2`\u01d6\3\2\2\2b\u01e3")
        buf.write("\3\2\2\2d\u01e5\3\2\2\2f\u01f3\3\2\2\2h\u01f5\3\2\2\2")
        buf.write("j\u01ff\3\2\2\2l\u0207\3\2\2\2n\u0209\3\2\2\2p\u020b\3")
        buf.write("\2\2\2r\u0215\3\2\2\2t\u021d\3\2\2\2v\u021f\3\2\2\2x\u0221")
        buf.write("\3\2\2\2z\u0231\3\2\2\2|\u0233\3\2\2\2~\u0247\3\2\2\2")
        buf.write("\u0080\u0255\3\2\2\2\u0082\u0258\3\2\2\2\u0084\u025b\3")
        buf.write("\2\2\2\u0086\u0265\3\2\2\2\u0088\u0269\3\2\2\2\u008a\u0271")
        buf.write("\3\2\2\2\u008c\u0277\3\2\2\2\u008e\u0090\5\4\3\2\u008f")
        buf.write("\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\7")
        buf.write("\2\2\3\u0094\3\3\2\2\2\u0095\u0096\7\30\2\2\u0096\u0099")
        buf.write("\7<\2\2\u0097\u0098\7;\2\2\u0098\u009a\7<\2\2\u0099\u0097")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009c\7\67\2\2\u009c\u009d\5\6\4\2\u009d\u009e\78\2\2")
        buf.write("\u009e\5\3\2\2\2\u009f\u00a0\5\n\6\2\u00a0\u00a1\5\b\5")
        buf.write("\2\u00a1\u00a4\3\2\2\2\u00a2\u00a4\3\2\2\2\u00a3\u009f")
        buf.write("\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\7\3\2\2\2\u00a5\u00a6")
        buf.write("\5\n\6\2\u00a6\u00a7\5\b\5\2\u00a7\u00aa\3\2\2\2\u00a8")
        buf.write("\u00aa\3\2\2\2\u00a9\u00a5\3\2\2\2\u00a9\u00a8\3\2\2\2")
        buf.write("\u00aa\t\3\2\2\2\u00ab\u00ae\5\f\7\2\u00ac\u00ae\5\26")
        buf.write("\f\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\13")
        buf.write("\3\2\2\2\u00af\u00b0\t\2\2\2\u00b0\u00b1\5\16\b\2\u00b1")
        buf.write("\u00b2\7;\2\2\u00b2\u00b5\5\24\13\2\u00b3\u00b4\7)\2\2")
        buf.write("\u00b4\u00b6\5*\26\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3")
        buf.write("\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\7:\2\2\u00b8\r")
        buf.write("\3\2\2\2\u00b9\u00ba\5\22\n\2\u00ba\u00bb\5\20\t\2\u00bb")
        buf.write("\17\3\2\2\2\u00bc\u00bd\79\2\2\u00bd\u00be\5\22\n\2\u00be")
        buf.write("\u00bf\5\20\t\2\u00bf\u00c2\3\2\2\2\u00c0\u00c2\3\2\2")
        buf.write("\2\u00c1\u00bc\3\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\21\3")
        buf.write("\2\2\2\u00c3\u00c4\t\3\2\2\u00c4\23\3\2\2\2\u00c5\u00c6")
        buf.write("\5\64\33\2\u00c6\25\3\2\2\2\u00c7\u00c8\t\3\2\2\u00c8")
        buf.write("\u00c9\7\63\2\2\u00c9\u00ca\5\30\r\2\u00ca\u00cb\7\64")
        buf.write("\2\2\u00cb\u00cc\5\u0088E\2\u00cc\u00d0\3\2\2\2\u00cd")
        buf.write("\u00d0\5$\23\2\u00ce\u00d0\5&\24\2\u00cf\u00c7\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\27\3\2")
        buf.write("\2\2\u00d1\u00d2\5\34\17\2\u00d2\u00d3\5\32\16\2\u00d3")
        buf.write("\u00d6\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00d1\3\2\2\2")
        buf.write("\u00d5\u00d4\3\2\2\2\u00d6\31\3\2\2\2\u00d7\u00d8\7:\2")
        buf.write("\2\u00d8\u00d9\5\34\17\2\u00d9\u00da\5\32\16\2\u00da\u00dd")
        buf.write("\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00d7\3\2\2\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dd\33\3\2\2\2\u00de\u00df\5\36\20\2")
        buf.write("\u00df\u00e0\7;\2\2\u00e0\u00e1\5\"\22\2\u00e1\35\3\2")
        buf.write("\2\2\u00e2\u00e3\7<\2\2\u00e3\u00e4\5 \21\2\u00e4\37\3")
        buf.write("\2\2\2\u00e5\u00e6\79\2\2\u00e6\u00e7\7<\2\2\u00e7\u00ea")
        buf.write("\5 \21\2\u00e8\u00ea\3\2\2\2\u00e9\u00e5\3\2\2\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00ea!\3\2\2\2\u00eb\u00ec\5\64\33\2\u00ec")
        buf.write("#\3\2\2\2\u00ed\u00ee\7\34\2\2\u00ee\u00ef\7\63\2\2\u00ef")
        buf.write("\u00f0\5\30\r\2\u00f0\u00f1\7\64\2\2\u00f1\u00f2\5\u0088")
        buf.write("E\2\u00f2%\3\2\2\2\u00f3\u00f4\7\35\2\2\u00f4\u00f5\7")
        buf.write("\63\2\2\u00f5\u00f6\7\64\2\2\u00f6\u00f7\5\u0088E\2\u00f7")
        buf.write("\'\3\2\2\2\u00f8\u00f9\7\20\2\2\u00f9\u00fa\7\63\2\2\u00fa")
        buf.write("\u00fb\5*\26\2\u00fb\u00fc\7\64\2\2\u00fc)\3\2\2\2\u00fd")
        buf.write("\u00fe\5L\'\2\u00fe\u00ff\5,\27\2\u00ff+\3\2\2\2\u0100")
        buf.write("\u0101\79\2\2\u0101\u0102\5L\'\2\u0102\u0103\5,\27\2\u0103")
        buf.write("\u0106\3\2\2\2\u0104\u0106\3\2\2\2\u0105\u0100\3\2\2\2")
        buf.write("\u0105\u0104\3\2\2\2\u0106-\3\2\2\2\u0107\u0108\7\20\2")
        buf.write("\2\u0108\u0109\7\63\2\2\u0109\u010a\5\60\31\2\u010a\u010b")
        buf.write("\7\64\2\2\u010b/\3\2\2\2\u010c\u010d\5(\25\2\u010d\u010e")
        buf.write("\5\62\32\2\u010e\61\3\2\2\2\u010f\u0110\79\2\2\u0110\u0111")
        buf.write("\5(\25\2\u0111\u0112\5\62\32\2\u0112\u0115\3\2\2\2\u0113")
        buf.write("\u0115\3\2\2\2\u0114\u010f\3\2\2\2\u0114\u0113\3\2\2\2")
        buf.write("\u0115\63\3\2\2\2\u0116\u011d\7\24\2\2\u0117\u011d\7\22")
        buf.write("\2\2\u0118\u011d\7\23\2\2\u0119\u011d\7\25\2\2\u011a\u011d")
        buf.write("\5\66\34\2\u011b\u011d\5<\37\2\u011c\u0116\3\2\2\2\u011c")
        buf.write("\u0117\3\2\2\2\u011c\u0118\3\2\2\2\u011c\u0119\3\2\2\2")
        buf.write("\u011c\u011a\3\2\2\2\u011c\u011b\3\2\2\2\u011d\65\3\2")
        buf.write("\2\2\u011e\u011f\7\20\2\2\u011f\u0120\7\65\2\2\u0120\u0121")
        buf.write("\58\35\2\u0121\u0122\79\2\2\u0122\u0123\5:\36\2\u0123")
        buf.write("\u0124\7\66\2\2\u0124\67\3\2\2\2\u0125\u0128\5\64\33\2")
        buf.write("\u0126\u0128\5\66\34\2\u0127\u0125\3\2\2\2\u0127\u0126")
        buf.write("\3\2\2\2\u01289\3\2\2\2\u0129\u012a\7\5\2\2\u012a;\3\2")
        buf.write("\2\2\u012b\u012c\7<\2\2\u012c=\3\2\2\2\u012d\u012e\7\65")
        buf.write("\2\2\u012e\u012f\5L\'\2\u012f\u0130\7\66\2\2\u0130\u0137")
        buf.write("\3\2\2\2\u0131\u0132\7\65\2\2\u0132\u0133\5L\'\2\u0133")
        buf.write("\u0134\7\66\2\2\u0134\u0135\5> \2\u0135\u0137\3\2\2\2")
        buf.write("\u0136\u012d\3\2\2\2\u0136\u0131\3\2\2\2\u0137?\3\2\2")
        buf.write("\2\u0138\u013d\5B\"\2\u0139\u013d\5D#\2\u013a\u013d\5")
        buf.write("H%\2\u013b\u013d\5F$\2\u013c\u0138\3\2\2\2\u013c\u0139")
        buf.write("\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("A\3\2\2\2\u013e\u013f\7\61\2\2\u013f\u0140\7<\2\2\u0140")
        buf.write("C\3\2\2\2\u0141\u0142\7<\2\2\u0142\u0143\7\62\2\2\u0143")
        buf.write("\u0144\7=\2\2\u0144E\3\2\2\2\u0145\u0146\7\61\2\2\u0146")
        buf.write("\u0147\7<\2\2\u0147\u0148\7\63\2\2\u0148\u0149\5*\26\2")
        buf.write("\u0149\u014a\7\64\2\2\u014aG\3\2\2\2\u014b\u014c\7<\2")
        buf.write("\2\u014c\u014d\7\62\2\2\u014d\u014e\7=\2\2\u014e\u0150")
        buf.write("\7\63\2\2\u014f\u0151\5*\26\2\u0150\u014f\3\2\2\2\u0150")
        buf.write("\u0151\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153\7\64\2")
        buf.write("\2\u0153I\3\2\2\2\u0154\u0155\7\36\2\2\u0155\u0156\7<")
        buf.write("\2\2\u0156\u0157\7\63\2\2\u0157\u0158\5*\26\2\u0158\u0159")
        buf.write("\7\64\2\2\u0159K\3\2\2\2\u015a\u015b\b\'\1\2\u015b\u015c")
        buf.write("\5N(\2\u015c\u0165\3\2\2\2\u015d\u015e\f\5\2\2\u015e\u015f")
        buf.write("\7\60\2\2\u015f\u0164\5L\'\6\u0160\u0161\f\4\2\2\u0161")
        buf.write("\u0162\7/\2\2\u0162\u0164\5L\'\5\u0163\u015d\3\2\2\2\u0163")
        buf.write("\u0160\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0165\u0166\3\2\2\2\u0166M\3\2\2\2\u0167\u0165\3\2\2")
        buf.write("\2\u0168\u0169\b(\1\2\u0169\u016a\5P)\2\u016a\u017f\3")
        buf.write("\2\2\2\u016b\u016c\f\t\2\2\u016c\u016d\7(\2\2\u016d\u017e")
        buf.write("\5N(\n\u016e\u016f\f\b\2\2\u016f\u0170\7*\2\2\u0170\u017e")
        buf.write("\5N(\t\u0171\u0172\f\7\2\2\u0172\u0173\7+\2\2\u0173\u017e")
        buf.write("\5N(\b\u0174\u0175\f\6\2\2\u0175\u0176\7-\2\2\u0176\u017e")
        buf.write("\5N(\7\u0177\u0178\f\5\2\2\u0178\u0179\7,\2\2\u0179\u017e")
        buf.write("\5N(\6\u017a\u017b\f\4\2\2\u017b\u017c\7.\2\2\u017c\u017e")
        buf.write("\5N(\5\u017d\u016b\3\2\2\2\u017d\u016e\3\2\2\2\u017d\u0171")
        buf.write("\3\2\2\2\u017d\u0174\3\2\2\2\u017d\u0177\3\2\2\2\u017d")
        buf.write("\u017a\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180O\3\2\2\2\u0181\u017f\3\2\2")
        buf.write("\2\u0182\u0183\b)\1\2\u0183\u0184\5R*\2\u0184\u018d\3")
        buf.write("\2\2\2\u0185\u0186\f\5\2\2\u0186\u0187\7&\2\2\u0187\u018c")
        buf.write("\5R*\2\u0188\u0189\f\4\2\2\u0189\u018a\7\'\2\2\u018a\u018c")
        buf.write("\5R*\2\u018b\u0185\3\2\2\2\u018b\u0188\3\2\2\2\u018c\u018f")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("Q\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0191\b*\1\2\u0191")
        buf.write("\u0192\5T+\2\u0192\u019b\3\2\2\2\u0193\u0194\f\5\2\2\u0194")
        buf.write("\u0195\7 \2\2\u0195\u019a\5T+\2\u0196\u0197\f\4\2\2\u0197")
        buf.write("\u0198\7!\2\2\u0198\u019a\5T+\2\u0199\u0193\3\2\2\2\u0199")
        buf.write("\u0196\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2")
        buf.write("\u019b\u019c\3\2\2\2\u019cS\3\2\2\2\u019d\u019b\3\2\2")
        buf.write("\2\u019e\u019f\b+\1\2\u019f\u01a0\5V,\2\u01a0\u01ac\3")
        buf.write("\2\2\2\u01a1\u01a2\f\6\2\2\u01a2\u01a3\7\"\2\2\u01a3\u01ab")
        buf.write("\5V,\2\u01a4\u01a5\f\5\2\2\u01a5\u01a6\7#\2\2\u01a6\u01ab")
        buf.write("\5V,\2\u01a7\u01a8\f\4\2\2\u01a8\u01a9\7$\2\2\u01a9\u01ab")
        buf.write("\5V,\2\u01aa\u01a1\3\2\2\2\u01aa\u01a4\3\2\2\2\u01aa\u01a7")
        buf.write("\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01adU\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af")
        buf.write("\u01b0\7%\2\2\u01b0\u01b3\5V,\2\u01b1\u01b3\5X-\2\u01b2")
        buf.write("\u01af\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3W\3\2\2\2\u01b4")
        buf.write("\u01b5\7!\2\2\u01b5\u01b8\5X-\2\u01b6\u01b8\5Z.\2\u01b7")
        buf.write("\u01b4\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8Y\3\2\2\2\u01b9")
        buf.write("\u01ba\b.\1\2\u01ba\u01bb\5\\/\2\u01bb\u01c0\3\2\2\2\u01bc")
        buf.write("\u01bd\f\4\2\2\u01bd\u01bf\5> \2\u01be\u01bc\3\2\2\2\u01bf")
        buf.write("\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1[\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c4\b/\1\2")
        buf.write("\u01c4\u01c5\5^\60\2\u01c5\u01cc\3\2\2\2\u01c6\u01c7\f")
        buf.write("\5\2\2\u01c7\u01cb\5B\"\2\u01c8\u01c9\f\4\2\2\u01c9\u01cb")
        buf.write("\5F$\2\u01ca\u01c6\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01ce")
        buf.write("\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd")
        buf.write("]\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf\u01d3\5D#\2\u01d0")
        buf.write("\u01d3\5H%\2\u01d1\u01d3\5`\61\2\u01d2\u01cf\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3_\3\2\2\2\u01d4")
        buf.write("\u01d7\5J&\2\u01d5\u01d7\5b\62\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d7a\3\2\2\2\u01d8\u01e4\7<\2\2\u01d9")
        buf.write("\u01e4\7=\2\2\u01da\u01e4\7\33\2\2\u01db\u01e4\7\27\2")
        buf.write("\2\u01dc\u01e4\7\5\2\2\u01dd\u01e4\7\7\2\2\u01de\u01e4")
        buf.write("\7\6\2\2\u01df\u01e4\7A\2\2\u01e0\u01e4\5(\25\2\u01e1")
        buf.write("\u01e4\5.\30\2\u01e2\u01e4\5d\63\2\u01e3\u01d8\3\2\2\2")
        buf.write("\u01e3\u01d9\3\2\2\2\u01e3\u01da\3\2\2\2\u01e3\u01db\3")
        buf.write("\2\2\2\u01e3\u01dc\3\2\2\2\u01e3\u01dd\3\2\2\2\u01e3\u01de")
        buf.write("\3\2\2\2\u01e3\u01df\3\2\2\2\u01e3\u01e0\3\2\2\2\u01e3")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4c\3\2\2\2\u01e5")
        buf.write("\u01e6\7\63\2\2\u01e6\u01e7\5L\'\2\u01e7\u01e8\7\64\2")
        buf.write("\2\u01e8e\3\2\2\2\u01e9\u01f4\5h\65\2\u01ea\u01f4\5p9")
        buf.write("\2\u01eb\u01f4\5x=\2\u01ec\u01f4\5|?\2\u01ed\u01f4\5~")
        buf.write("@\2\u01ee\u01f4\5\u0080A\2\u01ef\u01f4\5\u0082B\2\u01f0")
        buf.write("\u01f4\5\u0084C\2\u01f1\u01f4\5\u0086D\2\u01f2\u01f4\5")
        buf.write("\u0088E\2\u01f3\u01e9\3\2\2\2\u01f3\u01ea\3\2\2\2\u01f3")
        buf.write("\u01eb\3\2\2\2\u01f3\u01ec\3\2\2\2\u01f3\u01ed\3\2\2\2")
        buf.write("\u01f3\u01ee\3\2\2\2\u01f3\u01ef\3\2\2\2\u01f3\u01f0\3")
        buf.write("\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4g")
        buf.write("\3\2\2\2\u01f5\u01f6\7\32\2\2\u01f6\u01f7\5j\66\2\u01f7")
        buf.write("\u01f8\7;\2\2\u01f8\u01fb\5\24\13\2\u01f9\u01fa\7)\2\2")
        buf.write("\u01fa\u01fc\5*\26\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3")
        buf.write("\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe\7:\2\2\u01fei\3")
        buf.write("\2\2\2\u01ff\u0200\5n8\2\u0200\u0201\5l\67\2\u0201k\3")
        buf.write("\2\2\2\u0202\u0203\79\2\2\u0203\u0204\5n8\2\u0204\u0205")
        buf.write("\5l\67\2\u0205\u0208\3\2\2\2\u0206\u0208\3\2\2\2\u0207")
        buf.write("\u0202\3\2\2\2\u0207\u0206\3\2\2\2\u0208m\3\2\2\2\u0209")
        buf.write("\u020a\7<\2\2\u020ao\3\2\2\2\u020b\u020c\7\31\2\2\u020c")
        buf.write("\u020d\5r:\2\u020d\u020e\7;\2\2\u020e\u0211\5\24\13\2")
        buf.write("\u020f\u0210\7)\2\2\u0210\u0212\5*\26\2\u0211\u020f\3")
        buf.write("\2\2\2\u0211\u0212\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0214")
        buf.write("\7:\2\2\u0214q\3\2\2\2\u0215\u0216\5v<\2\u0216\u0217\5")
        buf.write("t;\2\u0217s\3\2\2\2\u0218\u0219\79\2\2\u0219\u021a\5v")
        buf.write("<\2\u021a\u021b\5t;\2\u021b\u021e\3\2\2\2\u021c\u021e")
        buf.write("\3\2\2\2\u021d\u0218\3\2\2\2\u021d\u021c\3\2\2\2\u021e")
        buf.write("u\3\2\2\2\u021f\u0220\7<\2\2\u0220w\3\2\2\2\u0221\u0222")
        buf.write("\5z>\2\u0222\u0223\7)\2\2\u0223\u0224\5L\'\2\u0224\u0225")
        buf.write("\7:\2\2\u0225y\3\2\2\2\u0226\u0232\7<\2\2\u0227\u0228")
        buf.write("\7<\2\2\u0228\u0232\5> \2\u0229\u022a\5L\'\2\u022a\u022b")
        buf.write("\5F$\2\u022b\u0232\3\2\2\2\u022c\u022d\5L\'\2\u022d\u022e")
        buf.write("\5B\"\2\u022e\u0232\3\2\2\2\u022f\u0232\5D#\2\u0230\u0232")
        buf.write("\5H%\2\u0231\u0226\3\2\2\2\u0231\u0227\3\2\2\2\u0231\u0229")
        buf.write("\3\2\2\2\u0231\u022c\3\2\2\2\u0231\u022f\3\2\2\2\u0231")
        buf.write("\u0230\3\2\2\2\u0232{\3\2\2\2\u0233\u0234\7\n\2\2\u0234")
        buf.write("\u0235\7\63\2\2\u0235\u0236\5L\'\2\u0236\u0237\7\64\2")
        buf.write("\2\u0237\u0240\5\u0088E\2\u0238\u0239\7\13\2\2\u0239\u023a")
        buf.write("\7\63\2\2\u023a\u023b\5L\'\2\u023b\u023c\7\64\2\2\u023c")
        buf.write("\u023d\5\u0088E\2\u023d\u023f\3\2\2\2\u023e\u0238\3\2")
        buf.write("\2\2\u023f\u0242\3\2\2\2\u0240\u023e\3\2\2\2\u0240\u0241")
        buf.write("\3\2\2\2\u0241\u0245\3\2\2\2\u0242\u0240\3\2\2\2\u0243")
        buf.write("\u0244\7\f\2\2\u0244\u0246\5\u0088E\2\u0245\u0243\3\2")
        buf.write("\2\2\u0245\u0246\3\2\2\2\u0246}\3\2\2\2\u0247\u0248\7")
        buf.write("\r\2\2\u0248\u0249\7\63\2\2\u0249\u024a\7<\2\2\u024a\u024b")
        buf.write("\7\21\2\2\u024b\u024c\5L\'\2\u024c\u024d\7\3\2\2\u024d")
        buf.write("\u0250\5L\'\2\u024e\u024f\7\37\2\2\u024f\u0251\5L\'\2")
        buf.write("\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u0252\3")
        buf.write("\2\2\2\u0252\u0253\7\64\2\2\u0253\u0254\5\u0088E\2\u0254")
        buf.write("\177\3\2\2\2\u0255\u0256\7\b\2\2\u0256\u0257\7:\2\2\u0257")
        buf.write("\u0081\3\2\2\2\u0258\u0259\7\t\2\2\u0259\u025a\7:\2\2")
        buf.write("\u025a\u0083\3\2\2\2\u025b\u025d\7\26\2\2\u025c\u025e")
        buf.write("\5L\'\2\u025d\u025c\3\2\2\2\u025d\u025e\3\2\2\2\u025e")
        buf.write("\u025f\3\2\2\2\u025f\u0260\7:\2\2\u0260\u0085\3\2\2\2")
        buf.write("\u0261\u0262\5L\'\2\u0262\u0263\5F$\2\u0263\u0266\3\2")
        buf.write("\2\2\u0264\u0266\5H%\2\u0265\u0261\3\2\2\2\u0265\u0264")
        buf.write("\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0268\7:\2\2\u0268")
        buf.write("\u0087\3\2\2\2\u0269\u026a\7\67\2\2\u026a\u026b\5\u008a")
        buf.write("F\2\u026b\u026c\78\2\2\u026c\u0089\3\2\2\2\u026d\u026e")
        buf.write("\5f\64\2\u026e\u026f\5\u008cG\2\u026f\u0272\3\2\2\2\u0270")
        buf.write("\u0272\3\2\2\2\u0271\u026d\3\2\2\2\u0271\u0270\3\2\2\2")
        buf.write("\u0272\u008b\3\2\2\2\u0273\u0274\5f\64\2\u0274\u0275\5")
        buf.write("\u008cG\2\u0275\u0278\3\2\2\2\u0276\u0278\3\2\2\2\u0277")
        buf.write("\u0273\3\2\2\2\u0277\u0276\3\2\2\2\u0278\u008d\3\2\2\2")
        buf.write("\63\u0091\u0099\u00a3\u00a9\u00ad\u00b5\u00c1\u00cf\u00d5")
        buf.write("\u00dc\u00e9\u0105\u0114\u011c\u0127\u0136\u013c\u0150")
        buf.write("\u0163\u0165\u017d\u017f\u018b\u018d\u0199\u019b\u01aa")
        buf.write("\u01ac\u01b2\u01b7\u01c0\u01ca\u01cc\u01d2\u01d6\u01e3")
        buf.write("\u01f3\u01fb\u0207\u0211\u021d\u0231\u0240\u0245\u0250")
        buf.write("\u025d\u0265\u0271\u0277")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'..'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Self'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'==.'", "'+.'", "'.'", "'::'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COMMENT", "INTEGER_LITERAL", 
                      "FLOAT_LITERAL", "BOOLEAN_LITERAL", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
                      "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
                      "RETURN", "NULL", "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                      "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
                      "STRING_EQUAL", "STRING_CONCAT", "DOT", "DOUBLE_COLON", 
                      "LP", "RP", "LSP", "RSP", "LCP", "RCP", "COMMA", "SEMI", 
                      "COLON", "ID", "DOLLAR_ID", "LETTER", "WS", "ERROR_CHAR", 
                      "STRING_LITERAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_declaration = 1
    RULE_memberlist = 2
    RULE_nextmember = 3
    RULE_member = 4
    RULE_attribute = 5
    RULE_list_of_attribute_names = 6
    RULE_next_attribute_name = 7
    RULE_attribute_name = 8
    RULE_type_name = 9
    RULE_method = 10
    RULE_list_of_parameters = 11
    RULE_next_parameter_dec = 12
    RULE_parameter_dec = 13
    RULE_id_list = 14
    RULE_next_id = 15
    RULE_typ = 16
    RULE_constructor = 17
    RULE_destructor = 18
    RULE_indexed_array = 19
    RULE_list_of_exp = 20
    RULE_next_exp = 21
    RULE_multi_dimen_arr = 22
    RULE_array_list = 23
    RULE_next_array = 24
    RULE_primitive_type = 25
    RULE_array_type = 26
    RULE_element_type = 27
    RULE_size = 28
    RULE_class_type = 29
    RULE_index_operator = 30
    RULE_member_access = 31
    RULE_instance_att_acc = 32
    RULE_static_att_acc = 33
    RULE_instance_met_inv = 34
    RULE_static_met_inv = 35
    RULE_object_creation = 36
    RULE_exp = 37
    RULE_exp1 = 38
    RULE_exp2 = 39
    RULE_exp3 = 40
    RULE_exp4 = 41
    RULE_exp5 = 42
    RULE_exp6 = 43
    RULE_exp7 = 44
    RULE_exp8 = 45
    RULE_exp9 = 46
    RULE_exp10 = 47
    RULE_operand = 48
    RULE_subexp = 49
    RULE_statement = 50
    RULE_variable_dec = 51
    RULE_list_of_variable_names = 52
    RULE_next_variable_name = 53
    RULE_variable_name = 54
    RULE_constant_dec = 55
    RULE_list_of_constant_names = 56
    RULE_next_constant_name = 57
    RULE_constant_name = 58
    RULE_assign_statement = 59
    RULE_lhs = 60
    RULE_if_statement = 61
    RULE_for_in_statement = 62
    RULE_break_statement = 63
    RULE_continue_statement = 64
    RULE_return_statement = 65
    RULE_method_inv_statement = 66
    RULE_block_statement = 67
    RULE_list_of_statement = 68
    RULE_next_statement = 69

    ruleNames =  [ "program", "class_declaration", "memberlist", "nextmember", 
                   "member", "attribute", "list_of_attribute_names", "next_attribute_name", 
                   "attribute_name", "type_name", "method", "list_of_parameters", 
                   "next_parameter_dec", "parameter_dec", "id_list", "next_id", 
                   "typ", "constructor", "destructor", "indexed_array", 
                   "list_of_exp", "next_exp", "multi_dimen_arr", "array_list", 
                   "next_array", "primitive_type", "array_type", "element_type", 
                   "size", "class_type", "index_operator", "member_access", 
                   "instance_att_acc", "static_att_acc", "instance_met_inv", 
                   "static_met_inv", "object_creation", "exp", "exp1", "exp2", 
                   "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", 
                   "exp10", "operand", "subexp", "statement", "variable_dec", 
                   "list_of_variable_names", "next_variable_name", "variable_name", 
                   "constant_dec", "list_of_constant_names", "next_constant_name", 
                   "constant_name", "assign_statement", "lhs", "if_statement", 
                   "for_in_statement", "break_statement", "continue_statement", 
                   "return_statement", "method_inv_statement", "block_statement", 
                   "list_of_statement", "next_statement" ]

    EOF = Token.EOF
    T__0=1
    COMMENT=2
    INTEGER_LITERAL=3
    FLOAT_LITERAL=4
    BOOLEAN_LITERAL=5
    BREAK=6
    CONTINUE=7
    IF=8
    ELSEIF=9
    ELSE=10
    FOREACH=11
    TRUE=12
    FALSE=13
    ARRAY=14
    IN=15
    INT=16
    FLOAT=17
    BOOLEAN=18
    STRING=19
    RETURN=20
    NULL=21
    CLASS=22
    VAL=23
    VAR=24
    SELF=25
    CONSTRUCTOR=26
    DESTRUCTOR=27
    NEW=28
    BY=29
    ADD=30
    SUB=31
    MUL=32
    DIV=33
    MOD=34
    NOT=35
    AND=36
    OR=37
    EQUAL=38
    ASSIGN=39
    NOT_EQUAL=40
    LESS=41
    LESS_OR_EQUAL=42
    GREATER=43
    GREATER_OR_EQUAL=44
    STRING_EQUAL=45
    STRING_CONCAT=46
    DOT=47
    DOUBLE_COLON=48
    LP=49
    RP=50
    LSP=51
    RSP=52
    LCP=53
    RCP=54
    COMMA=55
    SEMI=56
    COLON=57
    ID=58
    DOLLAR_ID=59
    LETTER=60
    WS=61
    ERROR_CHAR=62
    STRING_LITERAL=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 140
                self.class_declaration()
                self.state = 143 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 145
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LCP(self):
            return self.getToken(D96Parser.LCP, 0)

        def memberlist(self):
            return self.getTypedRuleContext(D96Parser.MemberlistContext,0)


        def RCP(self):
            return self.getToken(D96Parser.RCP, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(D96Parser.CLASS)
            self.state = 148
            self.match(D96Parser.ID)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 149
                self.match(D96Parser.COLON)
                self.state = 150
                self.match(D96Parser.ID)


            self.state = 153
            self.match(D96Parser.LCP)
            self.state = 154
            self.memberlist()
            self.state = 155
            self.match(D96Parser.RCP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def nextmember(self):
            return self.getTypedRuleContext(D96Parser.NextmemberContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memberlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberlist" ):
                return visitor.visitMemberlist(self)
            else:
                return visitor.visitChildren(self)




    def memberlist(self):

        localctx = D96Parser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memberlist)
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.member()
                self.state = 158
                self.nextmember()
                pass
            elif token in [D96Parser.RCP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NextmemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def nextmember(self):
            return self.getTypedRuleContext(D96Parser.NextmemberContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_nextmember

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextmember" ):
                return visitor.visitNextmember(self)
            else:
                return visitor.visitChildren(self)




    def nextmember(self):

        localctx = D96Parser.NextmemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nextmember)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.member()
                self.state = 164
                self.nextmember()
                pass
            elif token in [D96Parser.RCP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(D96Parser.AttributeContext,0)


        def method(self):
            return self.getTypedRuleContext(D96Parser.MethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_member)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.attribute()
                pass
            elif token in [D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.method()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_of_attribute_names(self):
            return self.getTypedRuleContext(D96Parser.List_of_attribute_namesContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(D96Parser.List_of_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = D96Parser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 174
            self.list_of_attribute_names()
            self.state = 175
            self.match(D96Parser.COLON)
            self.state = 176
            self.type_name()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 177
                self.match(D96Parser.ASSIGN)
                self.state = 178
                self.list_of_exp()


            self.state = 181
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_attribute_namesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_name(self):
            return self.getTypedRuleContext(D96Parser.Attribute_nameContext,0)


        def next_attribute_name(self):
            return self.getTypedRuleContext(D96Parser.Next_attribute_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_of_attribute_names

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_attribute_names" ):
                return visitor.visitList_of_attribute_names(self)
            else:
                return visitor.visitChildren(self)




    def list_of_attribute_names(self):

        localctx = D96Parser.List_of_attribute_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_of_attribute_names)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.attribute_name()
            self.state = 184
            self.next_attribute_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_attribute_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def attribute_name(self):
            return self.getTypedRuleContext(D96Parser.Attribute_nameContext,0)


        def next_attribute_name(self):
            return self.getTypedRuleContext(D96Parser.Next_attribute_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_next_attribute_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext_attribute_name" ):
                return visitor.visitNext_attribute_name(self)
            else:
                return visitor.visitChildren(self)




    def next_attribute_name(self):

        localctx = D96Parser.Next_attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_next_attribute_name)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(D96Parser.COMMA)
                self.state = 187
                self.attribute_name()
                self.state = 188
                self.next_attribute_name()
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_name" ):
                return visitor.visitAttribute_name(self)
            else:
                return visitor.visitChildren(self)




    def attribute_name(self):

        localctx = D96Parser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attribute_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_type_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = D96Parser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_of_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_of_parametersContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 198
                self.match(D96Parser.LP)
                self.state = 199
                self.list_of_parameters()
                self.state = 200
                self.match(D96Parser.RP)
                self.state = 201
                self.block_statement()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.destructor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_dec(self):
            return self.getTypedRuleContext(D96Parser.Parameter_decContext,0)


        def next_parameter_dec(self):
            return self.getTypedRuleContext(D96Parser.Next_parameter_decContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_of_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_parameters" ):
                return visitor.visitList_of_parameters(self)
            else:
                return visitor.visitChildren(self)




    def list_of_parameters(self):

        localctx = D96Parser.List_of_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_of_parameters)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.parameter_dec()
                self.state = 208
                self.next_parameter_dec()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_parameter_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def parameter_dec(self):
            return self.getTypedRuleContext(D96Parser.Parameter_decContext,0)


        def next_parameter_dec(self):
            return self.getTypedRuleContext(D96Parser.Next_parameter_decContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_next_parameter_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext_parameter_dec" ):
                return visitor.visitNext_parameter_dec(self)
            else:
                return visitor.visitChildren(self)




    def next_parameter_dec(self):

        localctx = D96Parser.Next_parameter_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_next_parameter_dec)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(D96Parser.SEMI)
                self.state = 214
                self.parameter_dec()
                self.state = 215
                self.next_parameter_dec()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(D96Parser.Id_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(D96Parser.TypContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameter_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_dec" ):
                return visitor.visitParameter_dec(self)
            else:
                return visitor.visitChildren(self)




    def parameter_dec(self):

        localctx = D96Parser.Parameter_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.id_list()
            self.state = 221
            self.match(D96Parser.COLON)
            self.state = 222
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def next_id(self):
            return self.getTypedRuleContext(D96Parser.Next_idContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = D96Parser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_id_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(D96Parser.ID)
            self.state = 225
            self.next_id()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def next_id(self):
            return self.getTypedRuleContext(D96Parser.Next_idContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_next_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext_id" ):
                return visitor.visitNext_id(self)
            else:
                return visitor.visitChildren(self)




    def next_id(self):

        localctx = D96Parser.Next_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_next_id)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(D96Parser.COMMA)
                self.state = 228
                self.match(D96Parser.ID)
                self.state = 229
                self.next_id()
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = D96Parser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_typ)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.primitive_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_of_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_of_parametersContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 236
            self.match(D96Parser.LP)
            self.state = 237
            self.list_of_parameters()
            self.state = 238
            self.match(D96Parser.RP)
            self.state = 239
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(D96Parser.DESTRUCTOR)
            self.state = 242
            self.match(D96Parser.LP)
            self.state = 243
            self.match(D96Parser.RP)
            self.state = 244
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(D96Parser.List_of_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indexed_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array" ):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_indexed_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(D96Parser.ARRAY)
            self.state = 247
            self.match(D96Parser.LP)
            self.state = 248
            self.list_of_exp()
            self.state = 249
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def next_exp(self):
            return self.getTypedRuleContext(D96Parser.Next_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_of_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_exp" ):
                return visitor.visitList_of_exp(self)
            else:
                return visitor.visitChildren(self)




    def list_of_exp(self):

        localctx = D96Parser.List_of_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list_of_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.exp(0)
            self.state = 252
            self.next_exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def next_exp(self):
            return self.getTypedRuleContext(D96Parser.Next_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_next_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext_exp" ):
                return visitor.visitNext_exp(self)
            else:
                return visitor.visitChildren(self)




    def next_exp(self):

        localctx = D96Parser.Next_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_next_exp)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.match(D96Parser.COMMA)
                self.state = 255
                self.exp(0)
                self.state = 256
                self.next_exp()
                pass
            elif token in [D96Parser.RP, D96Parser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_dimen_arrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def array_list(self):
            return self.getTypedRuleContext(D96Parser.Array_listContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multi_dimen_arr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_dimen_arr" ):
                return visitor.visitMulti_dimen_arr(self)
            else:
                return visitor.visitChildren(self)




    def multi_dimen_arr(self):

        localctx = D96Parser.Multi_dimen_arrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_multi_dimen_arr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(D96Parser.ARRAY)
            self.state = 262
            self.match(D96Parser.LP)
            self.state = 263
            self.array_list()
            self.state = 264
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def next_array(self):
            return self.getTypedRuleContext(D96Parser.Next_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = D96Parser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_array_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.indexed_array()
            self.state = 267
            self.next_array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_arrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def next_array(self):
            return self.getTypedRuleContext(D96Parser.Next_arrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_next_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext_array" ):
                return visitor.visitNext_array(self)
            else:
                return visitor.visitChildren(self)




    def next_array(self):

        localctx = D96Parser.Next_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_next_array)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(D96Parser.COMMA)
                self.state = 270
                self.indexed_array()
                self.state = 271
                self.next_array()
                pass
            elif token in [D96Parser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primitive_type)
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 278
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 279
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 280
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 281
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSP(self):
            return self.getToken(D96Parser.LSP, 0)

        def element_type(self):
            return self.getTypedRuleContext(D96Parser.Element_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def size(self):
            return self.getTypedRuleContext(D96Parser.SizeContext,0)


        def RSP(self):
            return self.getToken(D96Parser.RSP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(D96Parser.ARRAY)
            self.state = 285
            self.match(D96Parser.LSP)
            self.state = 286
            self.element_type()
            self.state = 287
            self.match(D96Parser.COMMA)
            self.state = 288
            self.size()
            self.state = 289
            self.match(D96Parser.RSP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_element_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_type" ):
                return visitor.visitElement_type(self)
            else:
                return visitor.visitChildren(self)




    def element_type(self):

        localctx = D96Parser.Element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_element_type)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = D96Parser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(D96Parser.INTEGER_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSP(self):
            return self.getToken(D96Parser.LSP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RSP(self):
            return self.getToken(D96Parser.RSP, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = D96Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_index_operator)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(D96Parser.LSP)
                self.state = 300
                self.exp(0)
                self.state = 301
                self.match(D96Parser.RSP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(D96Parser.LSP)
                self.state = 304
                self.exp(0)
                self.state = 305
                self.match(D96Parser.RSP)
                self.state = 306
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_att_acc(self):
            return self.getTypedRuleContext(D96Parser.Instance_att_accContext,0)


        def static_att_acc(self):
            return self.getTypedRuleContext(D96Parser.Static_att_accContext,0)


        def static_met_inv(self):
            return self.getTypedRuleContext(D96Parser.Static_met_invContext,0)


        def instance_met_inv(self):
            return self.getTypedRuleContext(D96Parser.Instance_met_invContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_access" ):
                return visitor.visitMember_access(self)
            else:
                return visitor.visitChildren(self)




    def member_access(self):

        localctx = D96Parser.Member_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_member_access)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.instance_att_acc()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.static_att_acc()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.static_met_inv()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 313
                self.instance_met_inv()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_att_accContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_att_acc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_att_acc" ):
                return visitor.visitInstance_att_acc(self)
            else:
                return visitor.visitChildren(self)




    def instance_att_acc(self):

        localctx = D96Parser.Instance_att_accContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_instance_att_acc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(D96Parser.DOT)
            self.state = 317
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_att_accContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_att_acc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_att_acc" ):
                return visitor.visitStatic_att_acc(self)
            else:
                return visitor.visitChildren(self)




    def static_att_acc(self):

        localctx = D96Parser.Static_att_accContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_static_att_acc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(D96Parser.ID)
            self.state = 320
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 321
            self.match(D96Parser.DOLLAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_met_invContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(D96Parser.List_of_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_met_inv

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_met_inv" ):
                return visitor.visitInstance_met_inv(self)
            else:
                return visitor.visitChildren(self)




    def instance_met_inv(self):

        localctx = D96Parser.Instance_met_invContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_instance_met_inv)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(D96Parser.DOT)
            self.state = 324
            self.match(D96Parser.ID)
            self.state = 325
            self.match(D96Parser.LP)
            self.state = 326
            self.list_of_exp()
            self.state = 327
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_met_invContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLE_COLON(self):
            return self.getToken(D96Parser.DOUBLE_COLON, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(D96Parser.List_of_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_met_inv

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_met_inv" ):
                return visitor.visitStatic_met_inv(self)
            else:
                return visitor.visitChildren(self)




    def static_met_inv(self):

        localctx = D96Parser.Static_met_invContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_static_met_inv)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(D96Parser.ID)
            self.state = 330
            self.match(D96Parser.DOUBLE_COLON)
            self.state = 331
            self.match(D96Parser.DOLLAR_ID)
            self.state = 332
            self.match(D96Parser.LP)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID) | (1 << D96Parser.STRING_LITERAL))) != 0):
                self.state = 333
                self.list_of_exp()


            self.state = 336
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_creationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(D96Parser.List_of_expContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_object_creation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_creation" ):
                return visitor.visitObject_creation(self)
            else:
                return visitor.visitChildren(self)




    def object_creation(self):

        localctx = D96Parser.Object_creationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_object_creation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(D96Parser.NEW)
            self.state = 339
            self.match(D96Parser.ID)
            self.state = 340
            self.match(D96Parser.LP)
            self.state = 341
            self.list_of_exp()
            self.state = 342
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(D96Parser.Exp1Context,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def STRING_CONCAT(self):
            return self.getToken(D96Parser.STRING_CONCAT, 0)

        def STRING_EQUAL(self):
            return self.getToken(D96Parser.STRING_EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 353
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 347
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 348
                        self.match(D96Parser.STRING_CONCAT)
                        self.state = 349
                        self.exp(4)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 350
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 351
                        self.match(D96Parser.STRING_EQUAL)
                        self.state = 352
                        self.exp(3)
                        pass

             
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Exp1Context,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(D96Parser.LESS, 0)

        def GREATER(self):
            return self.getToken(D96Parser.GREATER, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(D96Parser.LESS_OR_EQUAL, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(D96Parser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 379
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 361
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 362
                        self.match(D96Parser.EQUAL)
                        self.state = 363
                        self.exp1(8)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 364
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 365
                        self.match(D96Parser.NOT_EQUAL)
                        self.state = 366
                        self.exp1(7)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 367
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 368
                        self.match(D96Parser.LESS)
                        self.state = 369
                        self.exp1(6)
                        pass

                    elif la_ == 4:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 370
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 371
                        self.match(D96Parser.GREATER)
                        self.state = 372
                        self.exp1(5)
                        pass

                    elif la_ == 5:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 373
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 374
                        self.match(D96Parser.LESS_OR_EQUAL)
                        self.state = 375
                        self.exp1(4)
                        pass

                    elif la_ == 6:
                        localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 376
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 377
                        self.match(D96Parser.GREATER_OR_EQUAL)
                        self.state = 378
                        self.exp1(3)
                        pass

             
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 395
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 393
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 387
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 388
                        self.match(D96Parser.AND)
                        self.state = 389
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 390
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 391
                        self.match(D96Parser.OR)
                        self.state = 392
                        self.exp3(0)
                        pass

             
                self.state = 397
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(D96Parser.Exp3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 409
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 407
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 401
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 402
                        self.match(D96Parser.ADD)
                        self.state = 403
                        self.exp4(0)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 404
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 405
                        self.match(D96Parser.SUB)
                        self.state = 406
                        self.exp4(0)
                        pass

             
                self.state = 411
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(D96Parser.Exp4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 426
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 424
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 415
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 416
                        self.match(D96Parser.MUL)
                        self.state = 417
                        self.exp5()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 418
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 419
                        self.match(D96Parser.DIV)
                        self.state = 420
                        self.exp5()
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 421
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 422
                        self.match(D96Parser.MOD)
                        self.state = 423
                        self.exp5()
                        pass

             
                self.state = 428
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(D96Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = D96Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exp5)
        try:
            self.state = 432
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(D96Parser.NOT)
                self.state = 430
                self.exp5()
                pass
            elif token in [D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.SUB, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def exp6(self):
            return self.getTypedRuleContext(D96Parser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = D96Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp6)
        try:
            self.state = 437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(D96Parser.SUB)
                self.state = 435
                self.exp6()
                pass
            elif token in [D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.NEW, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.exp7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(D96Parser.Exp7Context,0)


        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.exp8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 446
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 442
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 443
                    self.index_operator() 
                self.state = 448
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(D96Parser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(D96Parser.Exp8Context,0)


        def instance_att_acc(self):
            return self.getTypedRuleContext(D96Parser.Instance_att_accContext,0)


        def instance_met_inv(self):
            return self.getTypedRuleContext(D96Parser.Instance_met_invContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.exp9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 458
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 456
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 452
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 453
                        self.instance_att_acc()
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                        self.state = 454
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 455
                        self.instance_met_inv()
                        pass

             
                self.state = 460
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_att_acc(self):
            return self.getTypedRuleContext(D96Parser.Static_att_accContext,0)


        def static_met_inv(self):
            return self.getTypedRuleContext(D96Parser.Static_met_invContext,0)


        def exp10(self):
            return self.getTypedRuleContext(D96Parser.Exp10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = D96Parser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_exp9)
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.static_att_acc()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.static_met_inv()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 463
                self.exp10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_creation(self):
            return self.getTypedRuleContext(D96Parser.Object_creationContext,0)


        def operand(self):
            return self.getTypedRuleContext(D96Parser.OperandContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = D96Parser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_exp10)
        try:
            self.state = 468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.object_creation()
                pass
            elif token in [D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.ARRAY, D96Parser.NULL, D96Parser.SELF, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(D96Parser.INTEGER_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(D96Parser.BOOLEAN_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def multi_dimen_arr(self):
            return self.getTypedRuleContext(D96Parser.Multi_dimen_arrContext,0)


        def subexp(self):
            return self.getTypedRuleContext(D96Parser.SubexpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = D96Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_operand)
        try:
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.match(D96Parser.DOLLAR_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 472
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 473
                self.match(D96Parser.NULL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 474
                self.match(D96Parser.INTEGER_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 475
                self.match(D96Parser.BOOLEAN_LITERAL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 476
                self.match(D96Parser.FLOAT_LITERAL)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 477
                self.match(D96Parser.STRING_LITERAL)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 478
                self.indexed_array()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 479
                self.multi_dimen_arr()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 480
                self.subexp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_subexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexp" ):
                return visitor.visitSubexp(self)
            else:
                return visitor.visitChildren(self)




    def subexp(self):

        localctx = D96Parser.SubexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_subexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(D96Parser.LP)
            self.state = 484
            self.exp(0)
            self.state = 485
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_dec(self):
            return self.getTypedRuleContext(D96Parser.Variable_decContext,0)


        def constant_dec(self):
            return self.getTypedRuleContext(D96Parser.Constant_decContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(D96Parser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(D96Parser.If_statementContext,0)


        def for_in_statement(self):
            return self.getTypedRuleContext(D96Parser.For_in_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(D96Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(D96Parser.Return_statementContext,0)


        def method_inv_statement(self):
            return self.getTypedRuleContext(D96Parser.Method_inv_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_statement)
        try:
            self.state = 497
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self.variable_dec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 488
                self.constant_dec()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 489
                self.assign_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 490
                self.if_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 491
                self.for_in_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 492
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 493
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 494
                self.return_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 495
                self.method_inv_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 496
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def list_of_variable_names(self):
            return self.getTypedRuleContext(D96Parser.List_of_variable_namesContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(D96Parser.List_of_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_dec" ):
                return visitor.visitVariable_dec(self)
            else:
                return visitor.visitChildren(self)




    def variable_dec(self):

        localctx = D96Parser.Variable_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_variable_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(D96Parser.VAR)
            self.state = 500
            self.list_of_variable_names()
            self.state = 501
            self.match(D96Parser.COLON)
            self.state = 502
            self.type_name()
            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 503
                self.match(D96Parser.ASSIGN)
                self.state = 504
                self.list_of_exp()


            self.state = 507
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_variable_namesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_name(self):
            return self.getTypedRuleContext(D96Parser.Variable_nameContext,0)


        def next_variable_name(self):
            return self.getTypedRuleContext(D96Parser.Next_variable_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_of_variable_names

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_variable_names" ):
                return visitor.visitList_of_variable_names(self)
            else:
                return visitor.visitChildren(self)




    def list_of_variable_names(self):

        localctx = D96Parser.List_of_variable_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_list_of_variable_names)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.variable_name()
            self.state = 510
            self.next_variable_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_variable_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def variable_name(self):
            return self.getTypedRuleContext(D96Parser.Variable_nameContext,0)


        def next_variable_name(self):
            return self.getTypedRuleContext(D96Parser.Next_variable_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_next_variable_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext_variable_name" ):
                return visitor.visitNext_variable_name(self)
            else:
                return visitor.visitChildren(self)




    def next_variable_name(self):

        localctx = D96Parser.Next_variable_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_next_variable_name)
        try:
            self.state = 517
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.match(D96Parser.COMMA)
                self.state = 513
                self.variable_name()
                self.state = 514
                self.next_variable_name()
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_name" ):
                return visitor.visitVariable_name(self)
            else:
                return visitor.visitChildren(self)




    def variable_name(self):

        localctx = D96Parser.Variable_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_variable_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def list_of_constant_names(self):
            return self.getTypedRuleContext(D96Parser.List_of_constant_namesContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_name(self):
            return self.getTypedRuleContext(D96Parser.Type_nameContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def list_of_exp(self):
            return self.getTypedRuleContext(D96Parser.List_of_expContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constant_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant_dec" ):
                return visitor.visitConstant_dec(self)
            else:
                return visitor.visitChildren(self)




    def constant_dec(self):

        localctx = D96Parser.Constant_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_constant_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.match(D96Parser.VAL)
            self.state = 522
            self.list_of_constant_names()
            self.state = 523
            self.match(D96Parser.COLON)
            self.state = 524
            self.type_name()
            self.state = 527
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 525
                self.match(D96Parser.ASSIGN)
                self.state = 526
                self.list_of_exp()


            self.state = 529
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_constant_namesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant_name(self):
            return self.getTypedRuleContext(D96Parser.Constant_nameContext,0)


        def next_constant_name(self):
            return self.getTypedRuleContext(D96Parser.Next_constant_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_of_constant_names

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_constant_names" ):
                return visitor.visitList_of_constant_names(self)
            else:
                return visitor.visitChildren(self)




    def list_of_constant_names(self):

        localctx = D96Parser.List_of_constant_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_list_of_constant_names)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self.constant_name()
            self.state = 532
            self.next_constant_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_constant_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def constant_name(self):
            return self.getTypedRuleContext(D96Parser.Constant_nameContext,0)


        def next_constant_name(self):
            return self.getTypedRuleContext(D96Parser.Next_constant_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_next_constant_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext_constant_name" ):
                return visitor.visitNext_constant_name(self)
            else:
                return visitor.visitChildren(self)




    def next_constant_name(self):

        localctx = D96Parser.Next_constant_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_next_constant_name)
        try:
            self.state = 539
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.match(D96Parser.COMMA)
                self.state = 535
                self.constant_name()
                self.state = 536
                self.next_constant_name()
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_constant_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant_name" ):
                return visitor.visitConstant_name(self)
            else:
                return visitor.visitChildren(self)




    def constant_name(self):

        localctx = D96Parser.Constant_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_constant_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.lhs()
            self.state = 544
            self.match(D96Parser.ASSIGN)
            self.state = 545
            self.exp(0)
            self.state = 546
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def index_operator(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorContext,0)


        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def instance_met_inv(self):
            return self.getTypedRuleContext(D96Parser.Instance_met_invContext,0)


        def instance_att_acc(self):
            return self.getTypedRuleContext(D96Parser.Instance_att_accContext,0)


        def static_att_acc(self):
            return self.getTypedRuleContext(D96Parser.Static_att_accContext,0)


        def static_met_inv(self):
            return self.getTypedRuleContext(D96Parser.Static_met_invContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_lhs)
        try:
            self.state = 559
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.match(D96Parser.ID)
                self.state = 550
                self.index_operator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 551
                self.exp(0)
                self.state = 552
                self.instance_met_inv()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 554
                self.exp(0)
                self.state = 555
                self.instance_att_acc()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 557
                self.static_att_acc()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 558
                self.static_met_inv()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LP)
            else:
                return self.getToken(D96Parser.LP, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RP)
            else:
                return self.getToken(D96Parser.RP, i)

        def block_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_statementContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_statementContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(D96Parser.IF)
            self.state = 562
            self.match(D96Parser.LP)
            self.state = 563
            self.exp(0)
            self.state = 564
            self.match(D96Parser.RP)
            self.state = 565
            self.block_statement()
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 566
                self.match(D96Parser.ELSEIF)
                self.state = 567
                self.match(D96Parser.LP)
                self.state = 568
                self.exp(0)
                self.state = 569
                self.match(D96Parser.RP)
                self.state = 570
                self.block_statement()
                self.state = 576
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 579
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 577
                self.match(D96Parser.ELSE)
                self.state = 578
                self.block_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_in_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpContext,i)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_in_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_statement" ):
                return visitor.visitFor_in_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_in_statement(self):

        localctx = D96Parser.For_in_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_for_in_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(D96Parser.FOREACH)
            self.state = 582
            self.match(D96Parser.LP)
            self.state = 583
            self.match(D96Parser.ID)
            self.state = 584
            self.match(D96Parser.IN)
            self.state = 585
            self.exp(0)
            self.state = 586
            self.match(D96Parser.T__0)
            self.state = 587
            self.exp(0)
            self.state = 590
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 588
                self.match(D96Parser.BY)
                self.state = 589
                self.exp(0)


            self.state = 592
            self.match(D96Parser.RP)
            self.state = 593
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.match(D96Parser.BREAK)
            self.state = 596
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
            self.match(D96Parser.CONTINUE)
            self.state = 599
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.match(D96Parser.RETURN)
            self.state = 603
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTEGER_LITERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.SELF) | (1 << D96Parser.NEW) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP) | (1 << D96Parser.ID) | (1 << D96Parser.DOLLAR_ID) | (1 << D96Parser.STRING_LITERAL))) != 0):
                self.state = 602
                self.exp(0)


            self.state = 605
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_inv_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def instance_met_inv(self):
            return self.getTypedRuleContext(D96Parser.Instance_met_invContext,0)


        def static_met_inv(self):
            return self.getTypedRuleContext(D96Parser.Static_met_invContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_inv_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_inv_statement" ):
                return visitor.visitMethod_inv_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_inv_statement(self):

        localctx = D96Parser.Method_inv_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_method_inv_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 607
                self.exp(0)
                self.state = 608
                self.instance_met_inv()
                pass

            elif la_ == 2:
                self.state = 610
                self.static_met_inv()
                pass


            self.state = 613
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCP(self):
            return self.getToken(D96Parser.LCP, 0)

        def list_of_statement(self):
            return self.getTypedRuleContext(D96Parser.List_of_statementContext,0)


        def RCP(self):
            return self.getToken(D96Parser.RCP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.match(D96Parser.LCP)
            self.state = 616
            self.list_of_statement()
            self.state = 617
            self.match(D96Parser.RCP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(D96Parser.StatementContext,0)


        def next_statement(self):
            return self.getTypedRuleContext(D96Parser.Next_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_of_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_statement" ):
                return visitor.visitList_of_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_of_statement(self):

        localctx = D96Parser.List_of_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_list_of_statement)
        try:
            self.state = 623
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.SELF, D96Parser.NEW, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.LCP, D96Parser.ID, D96Parser.DOLLAR_ID, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                self.statement()
                self.state = 620
                self.next_statement()
                pass
            elif token in [D96Parser.RCP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Next_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(D96Parser.StatementContext,0)


        def next_statement(self):
            return self.getTypedRuleContext(D96Parser.Next_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_next_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNext_statement" ):
                return visitor.visitNext_statement(self)
            else:
                return visitor.visitChildren(self)




    def next_statement(self):

        localctx = D96Parser.Next_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_next_statement)
        try:
            self.state = 629
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTEGER_LITERAL, D96Parser.FLOAT_LITERAL, D96Parser.BOOLEAN_LITERAL, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.NULL, D96Parser.VAL, D96Parser.VAR, D96Parser.SELF, D96Parser.NEW, D96Parser.SUB, D96Parser.NOT, D96Parser.LP, D96Parser.LCP, D96Parser.ID, D96Parser.DOLLAR_ID, D96Parser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 625
                self.statement()
                self.state = 626
                self.next_statement()
                pass
            elif token in [D96Parser.RCP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[37] = self.exp_sempred
        self._predicates[38] = self.exp1_sempred
        self._predicates[39] = self.exp2_sempred
        self._predicates[40] = self.exp3_sempred
        self._predicates[41] = self.exp4_sempred
        self._predicates[44] = self.exp7_sempred
        self._predicates[45] = self.exp8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 2)
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 2)
         




