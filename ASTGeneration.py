from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        res = []
        for i in range(0, ctx.getChildCount() - 1):
            res.append(self.visit(ctx.getChild(i)))
        return Program(res)

    def visitClassdecl(self, ctx:BKOOLParser.ClassdeclContext):
        classname = Id(ctx.ID(0).getText())
        memlist = self.visit(ctx.memberlist())
        parentname = Id(ctx.ID(1).getText()) if ctx.getChildCount() == 7 else None
        return ClassDecl(classname, memlist, parentname)

    def visitMemberlist(self, ctx:BKOOLParser.MemberlistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            member_list = self.visit(ctx.nextmember())
            member_list = self.visit(ctx.member()) + member_list
            # print(member_list)
            return member_list

    def visitNextmember(self, ctx:BKOOLParser.NextmemberContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            member_list = self.visit(ctx.nextmember())
            member_list = self.visit(ctx.member()) + member_list
            return member_list

    def visitMember(self, ctx:BKOOLParser.MemberContext):
        if ctx.methoddecl():
            return self.visit(ctx.methoddecl())
        elif ctx.attributedecl():
            return self.visit(ctx.attributedecl())
        elif ctx.constructor():
            return self.visit(ctx.constructor())

    def visitAttributedecl(self, ctx: BKOOLParser.AttributedeclContext):
        listattribute = self.visit(ctx.attnamelist())
        attnamelist = []
        for i in listattribute:
            # print(6)
            # print(i)
            if isinstance(i, tuple):
                kind = Static() if ctx.STATIC() else Instance()
                decl = ConstDecl(Id(i[0]), self.visit(ctx.typ()), i[1]) if ctx.FINAL() \
                    else \
                    VarDecl(Id(i[0]), self.visit(ctx.typ()), i[1])
                attnamelist.append(AttributeDecl(kind, decl))
            # print(7)
            # print(attnamelist)
        # print(8)
        # print(attnamelist)
        return attnamelist

    def visitAttnamelist(self, ctx:BKOOLParser.AttnamelistContext):
        # listattribute1 = self.visit(ctx.nextattributename())
        # print("3")
        # print(listattribute1)
        listattribute = self.visit(ctx.nextattributename())[::-1]
        # print("4")
        # print(listattribute)
        if ctx.exp():
            listattribute.insert(0, (ctx.ID().getText(), self.visit(ctx.exp())))
        else:
            listattribute.insert(0, (ctx.ID().getText(), None))
        # print("5")
        # print(listattribute)
        return listattribute

    def visitNextattributename(self, ctx:BKOOLParser.NextattributenameContext):
        if ctx.getChildCount() != 0:
            nextattributename = self.visit(ctx.nextattributename())
            # print("1")
            # print(nextattributename)
            if ctx.exp():
                nextattributename.append((ctx.ID().getText(), self.visit(ctx.exp())))
            else:
                nextattributename.append((ctx.ID().getText(), None))
            # print("2")
            # print(nextattributename)
            return nextattributename
        else:
            return []

    def visitMethoddecl(self, ctx: BKOOLParser.MethoddeclContext):
        paralist = self.visit(ctx.paralist())
        # print("paralist: ", paralist)
        methoddecl = []
        kind = Static() if ctx.STATIC() else Instance()
        name = ctx.ID().getText()
        returntype = self.visit(ctx.primitivetype())
        body = self.visit(ctx.blockstmt())
        # print("body: ", body)
        methoddecl.append(MethodDecl(kind, Id(name), paralist, returntype, body))
        return methoddecl

    def visitParalist(self, ctx:BKOOLParser.ParalistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            paradecl = self.visit(ctx.nextparadecl())
            paradecl = self.visit(ctx.paradecl()) + paradecl
            return paradecl

    def visitNextparadecl(self, ctx:BKOOLParser.NextparadeclContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            nextparadecl = self.visit(ctx.nextparadecl())
            nextparadecl = self.visit(ctx.paradecl()) + nextparadecl
            return nextparadecl

    def visitParadecl(self, ctx:BKOOLParser.ParadeclContext):
        idlist = self.visit(ctx.idlist())
        type = self.visit(ctx.typ())
        paradecl = []
        # print("idlist in paradecl: ", idlist)
        for i in idlist:
            # print("i: ", i, "\n")
            if isinstance(i, list):
                for j in i:
                    paradecl.append(j)
            else:
                paradecl.append(VarDecl(Id(i), type))
                # print("PARADECL: ", paradecl, "\n")
        return paradecl

    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        idlist = self.visit(ctx.nextid())[::-1]
        # print("idlist befor: ", idlist, "\n")
        idlist.insert(0, ctx.ID().getText())
        # print("idlist after: ", idlist, "\n")
        return idlist

    def visitNextid(self, ctx:BKOOLParser.NextidContext):
        if ctx.COMMA():
            nextid = self.visit(ctx.nextid())
            # print("nextid comma: ", nextid, "\n")
            nextid.append(ctx.ID().getText())
            # print("nextid comma after: ", nextid, "\n")
            return nextid
        elif ctx.SMCOLON():
            # newlist = self.visit(ctx.paradecl())
            # idlist2 = self.visit(ctx.nextid())
            # print("idlist2: ", idlist2)
            # print("newlist:", newlist)
            nextid = self.visit(ctx.nextid())
            # print("nextid sm: ", nextid, "\n")
            # for i in self.visit(ctx.paradecl()):
            #     nextid.append(i)
            nextid.append(self.visit(ctx.paradecl()))
            # print("nextid sm after: ", nextid, "\n")
            return nextid
        else:
            return []

    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        if ctx.blockstmt():
            return self.visit(ctx.blockstmt())
        elif ctx.asmstmt():
            return self.visit(ctx.asmstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        elif ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        elif ctx.methodinvocstmt():
            return self.visit(ctx.methodinvocstmt())

    def visitBlockstmt(self, ctx:BKOOLParser.BlockstmtContext):
        decl = self.visit(ctx.vardecllist())
        stmt = self.visit(ctx.stmtlist())
        # print("Block decl: ", decl, "Block stmt: ", stmt)
        return Block(decl, stmt)

    def visitVardecllist(self, ctx:BKOOLParser.VardecllistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            listvardec = self.visit(ctx.nextvardec())
            listvardec = self.visit(ctx.vardec()) + listvardec
            # print("listvardec: ", listvardec)
            return listvardec

    def visitNextvardec(self, ctx:BKOOLParser.NextvardecContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            listnextvar = self.visit(ctx.nextvardec())
            listnextvar = self.visit(ctx.vardec()) + listnextvar
            # print("listnextvar: ", listnextvar)
            return listnextvar

    def visitVardec(self, ctx:BKOOLParser.VardecContext):
        listattribute = self.visit(ctx.attnamelist())
        attnamelist = []
        for i in listattribute:
            # print("vardec list i: ", i)
            if isinstance(i, tuple):
                if ctx.FINAL():
                    attnamelist.append(ConstDecl(Id(i[0]), self.visit(ctx.typ()), i[1]))
                else:
                    attnamelist.append(VarDecl(Id(i[0]), self.visit(ctx.typ()), i[1]))
            # print("attnamelist in if: ", attnamelist)
        # print("return attnamelist: ", attnamelist)
        return attnamelist

    def visitStmtlist(self, ctx:BKOOLParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            stmtlist = self.visit(ctx.nextstmt())
            stmtlist = [self.visit(ctx.stmt())] + stmtlist
            # print("return stmtlist : ", stmtlist, "\n")
            return stmtlist

    def visitNextstmt(self, ctx:BKOOLParser.NextstmtContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            nextstmtlist = self.visit(ctx.nextstmt())
            # print("nextstmtlist is: ", nextstmtlist, "\n")
            nextstmtlist = [self.visit(ctx.stmt())] + nextstmtlist
            # print("return nextstmtlist is: ", nextstmtlist, "\n")
            return nextstmtlist

    def visitAsmstmt(self, ctx:BKOOLParser.AsmstmtContext):
        lhs = self.visit(ctx.exp(0))
        exp = self.visit(ctx.exp(1))
        return Assign(lhs, exp)

    def visitIfstmt(self, ctx:BKOOLParser.IfstmtContext):
        if ctx.getChildCount() == 6:
            exp = self.visit(ctx.exp())
            thenStmt = self.visit(ctx.stmt(0))
            elseStmt = self.visit(ctx.stmt(1))
            return If(exp, thenStmt, elseStmt)
        else:
            exp = self.visit(ctx.exp())
            thenStmt = self.visit(ctx.stmt(0))
            return If(exp, thenStmt)

    def visitForstmt(self, ctx:BKOOLParser.ForstmtContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        up = True if ctx.TO() else False
        loop = self.visit(ctx.stmt())
        return For(id, expr1, expr2, up, loop)

    def visitBreakstmt(self, ctx:BKOOLParser.BreakstmtContext):
        return Break()

    def visitContinuestmt(self, ctx:BKOOLParser.ContinuestmtContext):
        return Continue()

    def visitReturnstmt(self, ctx:BKOOLParser.ReturnstmtContext):
        expr = self.visit(ctx.exp())
        return Return(expr)

    def visitMethodinvocstmt(self, ctx:BKOOLParser.MethodinvocstmtContext):
        obj = self.visit(ctx.exp())
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.explist())
        return CallStmt(obj, method, param)

    def visitPrimitivetype(self, ctx:BKOOLParser.PrimitivetypeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.VOID():
            return VoidType()

    def visitConstructor(self, ctx: BKOOLParser.ConstructorContext):
        paralist = self.visit(ctx.paralist())
        methoddecl = []
        kind = Instance()
        name = Id("<init>")
        body = self.visit(ctx.blockstmt())
        methoddecl.append(MethodDecl(kind=kind,name=name,param=paralist,body=body,returnType=None))
        return methoddecl

    def visitExp(self, ctx:BKOOLParser.ExpContext):
        if ctx.LESS():
            return BinaryOp(ctx.LESS().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.GREATER():
            return BinaryOp(ctx.GREATER().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.LESSOE():
            return BinaryOp(ctx.LESSOE().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.GREATEROE():
            return BinaryOp(ctx.GREATEROE().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        else:
            return self.visit(ctx.exp1(0))
            # return "exp1"

    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        if ctx.EQ():
            return BinaryOp(ctx.EQ().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.NEQ():
            return BinaryOp(ctx.NEQ().getText(), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        else:
            return self.visit(ctx.exp2(0))
            # return "exp2"

    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        elif ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp3())

    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        elif ctx.SUB():
            return BinaryOp(ctx.SUB().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())
            # return "Exp4"

    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(),self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(),self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        elif ctx.FDIV():
            return BinaryOp(ctx.FDIV().getText(),self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        elif ctx.IDIV():
            return BinaryOp(ctx.IDIV().getText(),self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp5())

    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        if ctx.CONCAT():
            return BinaryOp(ctx.CONCAT().getText(),self.visit(ctx.exp5()),self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp6())

    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp7())

    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        if ctx.ADD():
            return UnaryOp(ctx.ADD().getText(), self.visit(ctx.exp7()))
        elif ctx.SUB():
            return UnaryOp(ctx.SUB().getText(), self.visit(ctx.exp7()))
        else:
            return self.visit(ctx.exp8())

    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        if ctx.index_op():
            value = self.visit(ctx.index_op())
            # print(10)
            # print(value)
            return ArrayCell(self.visit(ctx.exp8()), value)
        else:
            return self.visit(ctx.exp9())
            # return "exp9"

    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        if ctx.explist():
            return CallExpr(self.visit(ctx.exp9()), Id(ctx.ID().getText()), self.visit(ctx.explist()))
        elif ctx.getChildCount() == 3:
            return FieldAccess(self.visit(ctx.exp9()),Id(ctx.ID().getText()))
        else:
            return self.visit(ctx.exp10())
            # return "Exp10"

    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        if ctx.NEW():
            return NewExpr(self.visit(ctx.exp10()), self.visit(ctx.explist()))
        else:
            return self.visit(ctx.operand())

    def visitOperand(self, ctx:BKOOLParser.OperandContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLIT():
            if str(ctx.BOOLIT()) == "true":
                return BooleanLiteral(True)
            else:
                return BooleanLiteral(False)
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.THIS():
            return SelfLiteral()

    def visitIndex_op(self, ctx:BKOOLParser.Index_opContext):
        return self.visit(ctx.exp())

    def visitExplist(self, ctx:BKOOLParser.ExplistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            explist = self.visit(ctx.nextexp())
            explist = [self.visit(ctx.exp())] + explist
            return explist

    def visitNextexp(self, ctx:BKOOLParser.NextexpContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            explist = self.visit(ctx.nextexp())
            explist = [self.visit(ctx.exp())] + explist
            return explist

    def visitTyp(self, ctx: BKOOLParser.TypContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())
        elif ctx.classtype():
            return self.visit(ctx.classtype())

    def visitClasstype(self, ctx:BKOOLParser.ClasstypeContext):
        return ClassType(Id(ctx.ID().getText()))

    def visitArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        if ctx.INT():
            return ArrayType(int(ctx.INTLIT().getText()),IntType())
        if ctx.FLOAT():
            return ArrayType(int(ctx.INTLIT().getText()),FloatType())
        if ctx.BOOLEAN():
            return ArrayType(int(ctx.INTLIT().getText()),BoolType())
        if ctx.STRING():
            return ArrayType(int(ctx.INTLIT().getText()),StringType())

    def visitArraylit(self, ctx:BKOOLParser.ArraylitContext):
        value = list(map(lambda x: x.accept(self), ctx.literals()))
        # print("vale: ", value)
        return ArrayLiteral(value)

    def visitLiterals(self, ctx:BKOOLParser.LiteralsContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            if ctx.BOOLIT().getText() == "true":
                return BooleanLiteral(True)
            else:
                return BooleanLiteral(False)
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.nulliteral():
            return self.visit(ctx.nulliteral())

    def visitNulliteral(self, ctx:BKOOLParser.NulliteralContext):
        return NullLiteral()
