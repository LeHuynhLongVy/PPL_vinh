# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_declaration.
    def visitClass_declaration(self, ctx:D96Parser.Class_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memberlist.
    def visitMemberlist(self, ctx:D96Parser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#nextmember.
    def visitNextmember(self, ctx:D96Parser.NextmemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute.
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_attribute_names.
    def visitList_of_attribute_names(self, ctx:D96Parser.List_of_attribute_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#next_attribute_name.
    def visitNext_attribute_name(self, ctx:D96Parser.Next_attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_name.
    def visitAttribute_name(self, ctx:D96Parser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#type_name.
    def visitType_name(self, ctx:D96Parser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method.
    def visitMethod(self, ctx:D96Parser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_parameters.
    def visitList_of_parameters(self, ctx:D96Parser.List_of_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#next_parameter_dec.
    def visitNext_parameter_dec(self, ctx:D96Parser.Next_parameter_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter_dec.
    def visitParameter_dec(self, ctx:D96Parser.Parameter_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_list.
    def visitId_list(self, ctx:D96Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#next_id.
    def visitNext_id(self, ctx:D96Parser.Next_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typ.
    def visitTyp(self, ctx:D96Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#indexed_array.
    def visitIndexed_array(self, ctx:D96Parser.Indexed_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_exp.
    def visitList_of_exp(self, ctx:D96Parser.List_of_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#next_exp.
    def visitNext_exp(self, ctx:D96Parser.Next_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#multi_dimen_arr.
    def visitMulti_dimen_arr(self, ctx:D96Parser.Multi_dimen_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_list.
    def visitArray_list(self, ctx:D96Parser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#next_array.
    def visitNext_array(self, ctx:D96Parser.Next_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_type.
    def visitPrimitive_type(self, ctx:D96Parser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_type.
    def visitArray_type(self, ctx:D96Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_type.
    def visitElement_type(self, ctx:D96Parser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#size.
    def visitSize(self, ctx:D96Parser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_type.
    def visitClass_type(self, ctx:D96Parser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operator.
    def visitIndex_operator(self, ctx:D96Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member_access.
    def visitMember_access(self, ctx:D96Parser.Member_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_att_acc.
    def visitInstance_att_acc(self, ctx:D96Parser.Instance_att_accContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_att_acc.
    def visitStatic_att_acc(self, ctx:D96Parser.Static_att_accContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#instance_met_inv.
    def visitInstance_met_inv(self, ctx:D96Parser.Instance_met_invContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#static_met_inv.
    def visitStatic_met_inv(self, ctx:D96Parser.Static_met_invContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_creation.
    def visitObject_creation(self, ctx:D96Parser.Object_creationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp.
    def visitExp(self, ctx:D96Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp1.
    def visitExp1(self, ctx:D96Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp2.
    def visitExp2(self, ctx:D96Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp3.
    def visitExp3(self, ctx:D96Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp4.
    def visitExp4(self, ctx:D96Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp5.
    def visitExp5(self, ctx:D96Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp6.
    def visitExp6(self, ctx:D96Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp7.
    def visitExp7(self, ctx:D96Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp8.
    def visitExp8(self, ctx:D96Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp9.
    def visitExp9(self, ctx:D96Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp10.
    def visitExp10(self, ctx:D96Parser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operand.
    def visitOperand(self, ctx:D96Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#subexp.
    def visitSubexp(self, ctx:D96Parser.SubexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_dec.
    def visitVariable_dec(self, ctx:D96Parser.Variable_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_variable_names.
    def visitList_of_variable_names(self, ctx:D96Parser.List_of_variable_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#next_variable_name.
    def visitNext_variable_name(self, ctx:D96Parser.Next_variable_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#variable_name.
    def visitVariable_name(self, ctx:D96Parser.Variable_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constant_dec.
    def visitConstant_dec(self, ctx:D96Parser.Constant_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_constant_names.
    def visitList_of_constant_names(self, ctx:D96Parser.List_of_constant_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#next_constant_name.
    def visitNext_constant_name(self, ctx:D96Parser.Next_constant_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constant_name.
    def visitConstant_name(self, ctx:D96Parser.Constant_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_statement.
    def visitAssign_statement(self, ctx:D96Parser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_statement.
    def visitIf_statement(self, ctx:D96Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#for_in_statement.
    def visitFor_in_statement(self, ctx:D96Parser.For_in_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_statement.
    def visitBreak_statement(self, ctx:D96Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_statement.
    def visitContinue_statement(self, ctx:D96Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_statement.
    def visitReturn_statement(self, ctx:D96Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_inv_statement.
    def visitMethod_inv_statement(self, ctx:D96Parser.Method_inv_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_statement.
    def visitBlock_statement(self, ctx:D96Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_of_statement.
    def visitList_of_statement(self, ctx:D96Parser.List_of_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#next_statement.
    def visitNext_statement(self, ctx:D96Parser.Next_statementContext):
        return self.visitChildren(ctx)



del D96Parser