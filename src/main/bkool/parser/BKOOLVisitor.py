# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classDecle.
    def visitClassDecle(self, ctx:BKOOLParser.ClassDecleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#inheri.
    def visitInheri(self, ctx:BKOOLParser.InheriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classBody.
    def visitClassBody(self, ctx:BKOOLParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#members.
    def visitMembers(self, ctx:BKOOLParser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute.
    def visitAttribute(self, ctx:BKOOLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mulable.
    def visitMulable(self, ctx:BKOOLParser.MulableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutable.
    def visitImmutable(self, ctx:BKOOLParser.ImmutableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typAttribute.
    def visitTypAttribute(self, ctx:BKOOLParser.TypAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKOOLParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_type.
    def visitArray_type(self, ctx:BKOOLParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#size.
    def visitSize(self, ctx:BKOOLParser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_type.
    def visitClass_type(self, ctx:BKOOLParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#nonNullAttlist.
    def visitNonNullAttlist(self, ctx:BKOOLParser.NonNullAttlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attName.
    def visitAttName(self, ctx:BKOOLParser.AttNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprs.
    def visitExprs(self, ctx:BKOOLParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr6.
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr7.
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr8.
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr9.
    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr10.
    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operands.
    def visitOperands(self, ctx:BKOOLParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_list.
    def visitExpr_list(self, ctx:BKOOLParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#index_Expr.
    def visitIndex_Expr(self, ctx:BKOOLParser.Index_ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method.
    def visitMethod(self, ctx:BKOOLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#normalMethod.
    def visitNormalMethod(self, ctx:BKOOLParser.NormalMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#static_method.
    def visitStatic_method(self, ctx:BKOOLParser.Static_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#unstatic_method.
    def visitUnstatic_method(self, ctx:BKOOLParser.Unstatic_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typMethod.
    def visitTypMethod(self, ctx:BKOOLParser.TypMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramsList.
    def visitParamsList(self, ctx:BKOOLParser.ParamsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#params.
    def visitParams(self, ctx:BKOOLParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idList.
    def visitIdList(self, ctx:BKOOLParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_stmts.
    def visitBlock_stmts(self, ctx:BKOOLParser.Block_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecle.
    def visitVardecle(self, ctx:BKOOLParser.VardecleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmts.
    def visitStmts(self, ctx:BKOOLParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stmts.
    def visitAssign_stmts(self, ctx:BKOOLParser.Assign_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_stmts.
    def visitIf_stmts(self, ctx:BKOOLParser.If_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_stmts.
    def visitFor_stmts(self, ctx:BKOOLParser.For_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scalar_var.
    def visitScalar_var(self, ctx:BKOOLParser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_stmts.
    def visitBreak_stmts(self, ctx:BKOOLParser.Break_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_stmts.
    def visitContinue_stmts(self, ctx:BKOOLParser.Continue_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stmts.
    def visitReturn_stmts(self, ctx:BKOOLParser.Return_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#invocation_stmts.
    def visitInvocation_stmts(self, ctx:BKOOLParser.Invocation_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor.
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        return self.visitChildren(ctx)



del BKOOLParser