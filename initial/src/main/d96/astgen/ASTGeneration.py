from distutils.dep_util import newer
from re import L
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        classdecl = []
        for i in range(0, ctx.getChildCount() - 1):
            classdecl.append(self.visit(ctx.getChild(i)))
        return Program(classdecl)
    
    def visitClass_declaration(self, ctx: D96Parser.Class_declarationContext):
        classname = Id(ctx.ID(0).getText())
        memlist = self.visit(ctx.memberlist())
        parentname = Id(ctx.ID(1).getText()) if ctx.getChildCount() == 7 else None
        return ClassDecl(classname, memlist, parentname)
    
    def visitMemberlist(self, ctx: D96Parser.MemberlistContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            member_list = self.visit(ctx.nextmember())
            # print("member_list o 1: ", member_list)
            member_list = [self.visit(ctx.member())] + member_list
            # print("member_list o 2: ", member_list)
            return member_list
    
    def visitNextmember(self, ctx: D96Parser.NextmemberContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            member_list = self.visit(ctx.nextmember())
            # print("member_list o 3: ", member_list)
            member_list = self.visit(ctx.member()) + member_list
            # print("member_list o 4: ", member_list)
            return member_list
    
    def visitMember(self, ctx: D96Parser.MemberContext):
        if ctx.attribute():
            # print("member_list o duoc tra ve khi la attribute: ", self.visit(ctx.attribute()))
            return self.visit(ctx.attribute())
        elif ctx.method():
            return self.visit(ctx.method())
    
    def visitAttribute(self, ctx: D96Parser.AttributeContext):
        listattribute = self.visit(ctx.list_of_attribute_names()) # di lay list_of_attribute_name
        listexp = self.visit(ctx.list_of_exp()) if ctx.list_of_exp() else None # neu co list_of_exp thi di lay (visit) cai list_of_exp ve roi gan vo bien listexp. Con khong thi gan None cho no
        # print("value list: ", listexp)
        # print("attribute list : ", listattribute)
        
        res = [] # list dung ket qua de tra ve cho thang nao ma visit(ctx.attribute())
        for i in range(0, len(listattribute)): #lap qua tung thang trong 2 cai list tren
            # print("value list at i ", listexp[i])
            # print("attribute list at i: ", listattribute[i])
            
            kind = Static() if isinstance(listattribute[i],tuple) else Instance() # neu ma cai gia tri trong listattribute o vi tri i ma la tuple thi no la static, nguoc lai thi la instance 
            decl = ConstDecl(listattribute[i][0] if isinstance(listattribute[i],tuple) else listattribute[i], self.visit(ctx.type_name()), listexp[i] if listexp != None else None) if ctx.VAL() \
                        else \
                        VarDecl(listattribute[i][0] if isinstance(listattribute[i],tuple) else listattribute[i], self.visit(ctx.type_name()), listexp[i] if listexp != None else None)
            # decl se la ConstDecl neu co ctx.VAL(). Con khong thi no la VarDecl
            # Trong cai ConstDecl vs Vardecl: Neu cai phan tu listattribute[i] ma la tuple thi chi in thang dau ra thoi
            # Con khong thi in het no ra
            # 
            # Gia tri khoi tao (value) thi neu co khai bao = 5 thi listattribute[i] = 5, con neu ma khong khai bao gia tri khoi tao, cai listexp = None
            # Va khi no bang None thi khong de yen no la None 
            # Cai type_name thi phai di lay no ve. 
            res.append(AttributeDecl(kind, decl))
        # print("member_list o duoc tra ve khi la res -> attribute: ", res)
        return res

    def visitType_name(self, ctx: D96Parser.Type_nameContext):
        return self.visit(ctx.primitive_type())

    def visitPrimitive_type(self, ctx: D96Parser.Primitive_typeContext):
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.array_type():
            return self.visit(ctx.array_type())
        if ctx.class_type():
            return self.visit(ctx.class_type())
    
    def visitArray_type(self, ctx: D96Parser.Array_typeContext):
        size = self.visit(ctx.size())
        eleType = self.visit(ctx.element_type())
        return ArrayType(size, eleType)

    def visitElement_type(self, ctx: D96Parser.Element_typeContext):
        if ctx.primitive_type():
            return self.visit(ctx.primitive_type())
        else:
            return self.visit(ctx.array_type())

    def visitSize(self, ctx: D96Parser.SizeContext):
        return int(ctx.INTEGER_LITERAL().getText())

    def visitClass_type(self, ctx: D96Parser.Class_typeContext):
        return ClassType(ctx.ID().getText())

    def visitList_of_attribute_names(self, ctx: D96Parser.List_of_constant_namesContext):
        list_of_attribute_names = self.visit(ctx.next_attribute_name())
        list_of_attribute_names = [self.visit(ctx.attribute_name())] + list_of_attribute_names
        return list_of_attribute_names
    
    def visitNext_attribute_name(self, ctx: D96Parser.Next_attribute_nameContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            list_of_attribute_names = self.visit(ctx.next_attribute_name())
            list_of_attribute_names = [self.visit(ctx.attribute_name())] + list_of_attribute_names
            return list_of_attribute_names
    
    def visitAttribute_name(self, ctx: D96Parser.Attribute_nameContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.DOLLAR_ID():
            return (Id(ctx.DOLLAR_ID().getText()),1)
    
    def visitMethod(self, ctx: D96Parser.MethodContext):
        if ctx.constructor():
            kind = Instance()
            name = Id("Constructor")
            param,body = self.visit(ctx.constructor())
            return MethodDecl(kind,name,param,body)
        elif ctx.destructor():
            kind = Instance()
            name = Id("Destructor")
            param,body = self.visit(ctx.destructor())
            return MethodDecl(kind,name,param,body)
        else:
            if ctx.ID():
                kind = Instance()
                name = Id(ctx.ID().getText())
                param = self.visit(ctx.list_of_parameters())
                body = self.visit(ctx.block_statement())
                return MethodDecl(kind,name,param,body)
            elif ctx.DOLLAR_ID():
                kind = Static()
                name = Id(ctx.DOLLAR_ID().getText())
                param = self.visit(ctx.list_of_parameters())
                body = self.visit(ctx.block_statement())
                return MethodDecl(kind,name,param,body)

    def visitList_of_parameters(self, ctx: D96Parser.List_of_parametersContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            list_of_parameters = self.visit(ctx.next_parameter_dec())
            list_of_parameters = [self.visit(ctx.parameter_dec())] + list_of_parameters
            return list_of_parameters

    def visitNext_parameter_dec(self, ctx: D96Parser.Next_parameter_decContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            list_of_parameters = self.visit(ctx.next_parameter_dec())
            list_of_parameters = [self.visit(ctx.parameter_dec())] + list_of_parameters
            return list_of_parameters

    def visitParameter_dec(self, ctx: D96Parser.Parameter_decContext):
        res =[]
        idlist = self.visit(ctx.id_list())
        typ = self.visit(ctx.typ())
        for i in idlist:
            res.append(VarDecl(i,typ)) 
        return res
    
    def visitId_list(self, ctx: D96Parser.Id_listContext):
        idlist = self.visit(ctx.next_id())
        idlist = [ctx.ID().getText()] + idlist
        return idlist

    def visitNext_id(self, ctx: D96Parser.Next_idContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            idlist = self.visit(ctx.next_id())
            idlist = [ctx.ID().getText()] + idlist
            return idlist
    
    def visitTyp(self, ctx: D96Parser.TypContext):
        return self.visit(ctx.primitive_type())
    
    def visitExp(self, ctx: D96Parser.ExpContext):
        if ctx.STRING_CONCAT():
            return BinaryOp(ctx.STRING_CONCAT().getText(), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)))
        elif ctx.STRING_EQUAL():
            return BinaryOp(ctx.STRING_EQUAL().getText(), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)))
        else:
            return self.visit(ctx.exp1())
    
    def visitExp1(self, ctx: D96Parser.Exp1Context):
        if ctx.EQUAL():
            return BinaryOp(ctx.EQUAL().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.NOT_EQUAL():
            return BinaryOp(ctx.NOT_EQUAL().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.LESS():
            return BinaryOp(ctx.LESS().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.GREATER():
            return BinaryOp(ctx.GREATER().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.LESS_OR_EQUAL():
            return BinaryOp(ctx.LESS_OR_EQUAL().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        elif ctx.GREATER_OR_EQUAL():
            return BinaryOp(ctx.GREATER_OR_EQUAL().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))
        else:
            return self.visit(ctx.exp2())
        
    def visitExp2(self, ctx: D96Parser.Exp2Context):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        elif ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp3())
    
    def visitExp3(self, ctx: D96Parser.Exp3Context):
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        elif ctx.SUB():
            return BinaryOp(ctx.SUB().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())
    
    def visitExp4(self, ctx: D96Parser.Exp4Context):
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        elif ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), self.visit(ctx.exp4()), self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp5())
    
    def visitExp5(self, ctx: D96Parser.Exp5Context):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp6())

    def visitExp6(self, ctx: D96Parser.Exp6Context):
        if ctx.SUB():
            return UnaryOp(ctx.SUB().getText(), self.visit(ctx.exp6()))
        else:
            return self.visit(ctx.exp7())  

    def visitExp7(self, ctx: D96Parser.Exp7Context):
        if ctx.index_operator():
            idx = self.visit(ctx.index_operator())
            return ArrayCell(self.visit(ctx.exp7()),idx)
        else: 
            return self.visit(ctx.exp8())

    def visitIndex_operator(self, ctx: D96Parser.Index_operatorContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.index_operator())
    
    def visitExp8(self, ctx: D96Parser.Exp8Context):
        if ctx.instance_att_acc():
            return FieldAccess(self.visit(ctx.exp8()), self.visit(ctx.instance_att_acc()))
        elif ctx.instance_met_inv():
            method_exp_list = self.visit(ctx.instance_met_inv())
            method = method_exp_list[0]
            param = method_exp_list[1::]
            return CallExpr(self.visit(ctx.exp8()), method=method, param=param)
        else:
            return self.visit(ctx.exp9())
            
    def visitExp9(self, ctx: D96Parser.Exp9Context):
        if ctx.static_att_acc():
            return self.visit(ctx.static_att_acc())
        elif ctx.static_met_inv():
            return self.visit(ctx.static_met_inv())
        else:
            return self.visit(ctx.exp10())

    def visitStatic_att_acc(self, ctx: D96Parser.Static_att_accContext):
        return FieldAccess(ctx.ID().getText(),ctx.DOLLAR_ID().getText())
    
    def visitStatic_met_inv(self, ctx: D96Parser.Static_met_invContext):
        return CallExpr(ctx.ID().getText(), ctx.DOLLAR_ID().getText(), self.visit(ctx.list_of_exp()))

    def visitExp10(self, ctx: D96Parser.Exp10Context):
        if ctx.object_creation():
            return self.visit(ctx.object_creation())
        elif ctx.operand():
            return self.visit(ctx.operand())
    
    def visitObject_creation(self, ctx: D96Parser.Object_creationContext):
        return NewExpr(ctx.ID().getText(), self.visit(ctx.list_of_exp()))
    
    def visitOperand(self, ctx: D96Parser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.DOLLAR_ID():
            return Id(ctx.DOLLAR_ID().getText())
        elif ctx.SELF():
            return SelfLiteral()
        elif ctx.NULL():
            return NullLiteral()
        elif ctx.INTEGER_LITERAL():
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))
        elif ctx.BOOLEAN_LITERAL():
            if ctx.BOOLEAN_LITERAL().getText() == "True":
                return BooleanLiteral(True)
            else:
                return BooleanLiteral(False)
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.indexed_array():
            return self.visit(ctx.indexed_array())
        elif ctx.multi_dimen_arr():
            return self.visit(ctx.multi_dimen_arr())
        elif ctx.subexp():
            return self.visit(ctx.subexp())
    
    def visitSubexp(self, ctx: D96Parser.SubexpContext):
        return self.visit(ctx.exp())

    def visitList_of_exp(self, ctx: D96Parser.List_of_expContext):
        list_of_exp = self.visit(ctx.next_exp())
        list_of_exp = [self.visit(ctx.exp())] + list_of_exp
        return list_of_exp

    def visitNext_exp(self, ctx: D96Parser.Next_expContext):
        if ctx.getChildCount() == 0:
            return []
        list_of_exp = self.visit(ctx.next_exp())
        list_of_exp = [self.visit(ctx.exp())] + list_of_exp
        return list_of_exp

    def visitBlock_statement(self, ctx: D96Parser.Block_statementContext):
        liststmt = self.visit(ctx.list_of_statement())
        return Block(liststmt)
    
    def visitList_of_statement(self, ctx: D96Parser.List_of_statementContext):
        if ctx.getChildCount() == 0:
            return []
        list_of_stmt = self.visit(ctx.next_statement())
        list_of_stmt = [self.visit(ctx.statement())] + list_of_stmt
        return list_of_stmt
    
    def visitNext_statement(self, ctx: D96Parser.Next_statementContext):
        if ctx.getChildCount() == 0:
            return []
        list_of_stmt = self.visit(ctx.next_statement())
        list_of_stmt = [self.visit(ctx.statement())] + list_of_stmt
        return list_of_stmt
    
    def visitStatement(self, ctx: D96Parser.StatementContext):
        if ctx.variable_dec():
            return self.visit(ctx.variable_dec())
        elif ctx.constant_dec():
            return self.visit(ctx.constant_dec())
        elif ctx.assign_statement():
            return self.visit(ctx.assign_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.for_in_statement():
            return self.visit(ctx.for_in_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.method_inv_statement():
            return self.visit(ctx.method_inv_statement())
        elif ctx.block_statement():
            return self.visit(ctx.block_statement())
    
    def visitAssign_statement(self, ctx: D96Parser.Assign_statementContext):
        lhs = self.visit(ctx.lhs())
        expr = self.visit(ctx.exp())
        return Assign(lhs, expr)

    def visitLhs(self, ctx: D96Parser.LhsContext):
        if ctx.getChildCount() == 1 and ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.getChildCount() == 2 and ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.index_operator()))
    
    def visitFor_in_statement(self, ctx: D96Parser.For_in_statementContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        expr3 = self.visit(ctx.exp(2)) if ctx.exp(2) else None
        loop = self.visit(ctx.block_statement())
        return For(id,expr1,expr2,loop,expr3)
    
    def visitBreak_statement(self, ctx: D96Parser.Break_statementContext):
        return Break()
    
    def visitContinue_statement(self, ctx: D96Parser.Continue_statementContext):
        return Continue()
    
    def visitReturn_statement(self, ctx: D96Parser.Return_statementContext):
        return Return(self.visit(ctx.exp()) if ctx.exp() else None)
    
    def visitMethod_inv_statement(self, ctx: D96Parser.Method_inv_statementContext):
        if ctx.instance_met_inv():
            obj = self.visit(ctx.exp())
            methodandparam = self.visit(ctx.instance_met_inv())
            method = methodandparam[0][0]  
            param = methodandparam[0][1]
            return CallStmt(obj,method,param)
        elif ctx.static_met_inv():
            return self.visit(ctx.static_met_inv())
    
    def visitInstance_met_inv(self, ctx: D96Parser.Instance_met_invContext):
        res = []
        method = ctx.ID().getText()
        param = self.visit(ctx.list_of_exp())
        res.apend((method,param))
        return res
    
    
