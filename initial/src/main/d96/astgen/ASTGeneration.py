from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        classdecl = []
        for i in range(0, ctx.getChildCount() - 1):
            res.append(self.visit(ctx.getChild(i)))
        return Program(classdecl)
    
    def visitClass_declaration(self, ctx: D96Parser.ProgramContext):
        classname = Id(ctx.ID(0).getText())
        memlist = self.visit(ctx.memberlist())
        parentname = Id(ctx.ID(1).getText()) if ctx.getChildCount() == 7 else None
        return ClassDecl(classname, memlist, parentname)
    
    def visitMemberlist(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            member_list = self.visit(ctx.nextmember())
            member_list = self.visit(ctx.member()) + member_list
            # print(member_list)
            return member_list
    
    def visitNextmember(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            member_list = self.visit(ctx.nextmember())
            member_list = self.visit(ctx.member()) + member_list
            return member_list
    
    def visitMember(self, ctx: D96Parser.ProgramContext):
        if ctx.attribute():
            return self.visit(ctx.attribute())
        elif ctx.method():
            return self.visit(ctx.method())
    
    def visitAttribute(self, ctx: D96Parser.ProgramContext):
        listattribute = self.visit(ctx.list_of_attribute_names())
        listexp = self.visit(ctx.list_of_exp())
        res = []
        for i in range(0, listattribute - 1):
            kind = Static() if "$" in listattribute(i) else Instance()
            decl = ConstDecl(Id(listattribute(i)), self.visit(ctx.type_name()), listexp(i)) if ctx.VAL() \
                        else \
                        VarDecl(Id(listattribute(i)), self.visit(ctx.type_name()), listexp(i))
            
            res.append(AttributeDecl(kind, decl))

            return res
    
    def visitList_of_attribute_names(self, ctx: D96Parser.ProgramContext):
        list_of_attribute_names = self.visit(ctx.next_attribute_name())
        list_of_attribute_names = self.visit(ctx.attribute_name()) + list_of_attribute_names
        return list_of_attribute_names
    
    def visitNext_attribute_name(self, ctx: D96Parser.ProgramContext):
        if ctx.getChildCount() == 0:
            return []
        else:
            list_of_attribute_names = self.visit(ctx.next_attribute_name())
            list_of_attribute_names = self.visit(ctx.attribute_name()) + list_of_attribute_names
            return list_of_attribute_names
    
    def visitAttribute_name(self, ctx: D96Parser.ProgramContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.DOLLAR_ID():
            return Id(ctx.DOLLAR_ID().getText())
    
    


