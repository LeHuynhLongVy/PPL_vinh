import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Class Shape {
            Var $a,b : Int = 5,6;
        }"""
        expect = str(Program([ClassDecl(classname=Id("Shape"),memlist=[AttributeDecl(kind=Instance(),decl=ConstDecl(constant=Id("a"),constType=IntType(),value=IntLiteral(5)))])]))
        self.assertTrue(TestAST.test(input,expect,300))

    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """Class Shape : circle {}"""
    #     expect = str(Program([ClassDecl(classname=Id("Shape"),parentname=Id("circle"),memlist=[])]))
    #     self.assertTrue(TestAST.test(input,expect,301))
   