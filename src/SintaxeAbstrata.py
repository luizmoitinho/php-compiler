from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

# ========== CLASSES ABSTRATAS ================

class Main(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Main_MainProgram(Main):
  def __init__(self, mainInner):
    self.mainInner = mainInner
  def accept(self, Visitor):
    return Visitor.visitMain_MainProgram(self)
    
class Main_Empty(Main):
  def accept(self, Visitor):
    return Visitor.visitMain_Empty()

#MAIN_INNER ABSTRATA E CONCRETAS  
class MainInner(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class MainProgram_InnerStatement_Recursive(MainInner):
  def __init__(self, innerStatement, mainInner):
    self.innerStatement = innerStatement
    self.mainInner = mainInner
  def accept(self, Visitor):
    return Visitor.visitMainProgram_InnerStatement_Recursive(self)

class MainProgram_InnerStatement(MainInner):
  def __init__(self, innerStatement):
    self.innerStatement = innerStatement
  def accept(self, Visitor):
    return Visitor.visitMainProgram_InnerStatement(self)

class InnerStatement(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass
    
class InnerStatement_Statement(InnerStatement):
  def __init__(self, statement):
    self.statement = statement
  def accept(self, Visitor):
    return Visitor.visitInnerStatement_Statement(self)
    
class InnerStatement_FuncDecStatement(InnerStatement):
  def __init__(self, funcDecStatement):
    self.funcDecStatement = funcDecStatement
  def accept(self, Visitor):
    return Visitor.visitInnerStatement_FuncDecStatement(self)
    
class InnerStatementMul(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class InnerStatementMul_Mul(InnerStatementMul):
  def __init__(self, innerStatement, innerStatementMul):
    self.innerStatement = innerStatement
    self.innerStatementMul = innerStatementMul
  def accept(self, Visitor):
    return Visitor.visitInnerStatementMul_Mul(self)

class InnerStatementMul_Single(InnerStatementMul):
  def __init__(self, innerStatement):
    self.innerStatement = innerStatement
  def accept(self, Visitor):
    return Visitor.visitInnerStatementMul_Single(self)

class Statement(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class StatementBlockOpt(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class StatementBlockOpt_Statement(StatementBlockOpt):
  def __init__(self, statement):
    self.statement =  statement
  def accept(self, Visitor):
    return Visitor.visitStatementBlockOpt_Statement(self)

class StatementBlockOpt_ParenEmpty(StatementBlockOpt):
  def accept(self, Visitor):
    return Visitor.visitStatementBlockOpt_ParenEmpty(self)

class StatementBlockOpt_StatementMul(StatementBlockOpt):
  def __init__(self, statementmul):
    self.statementmul = statementmul
  def accept(self, Visitor):
    return Visitor.visitStatementBlockOpt_StatementMul(self)

class StatementMul(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class StatementMul_Mul(StatementMul):
  def __init__(self, statement,statementMul):
    self.statement = statement
    self.statementMul = statementMul
  def accept(self, Visitor):
    return Visitor.visitStatementMul_Mul(self)

class Statement_Expr(Statement):
  def __init__(self, expr, semiColon):
    self.expr = expr
    self.semiColon = semiColon
  def accept(self, Visitor):
    return Visitor.visitStatement_Expr(self)
    
class Statement_Break(Statement):
  def __init__(self, _break):
    self._break = _break
  def accept(self, Visitor):
    return Visitor.visitStatement_Break(self)
    
class Statement_Continue(Statement):
  def __init__(self, _continue):
    self._continue = _continue
  def accept(self, Visitor):
    return Visitor.visitStatement_Continue(self)
    
class Statement_Return(Statement):
  def __init__(self, _return):
    self._return = _return
  def accept(self, Visitor):
    return Visitor.visitStatement_Return(self)
  
class Statement_Exit(Statement):
  def __init__(self, exit):
    self.exit = exit
  def accept(self, Visitor):
    return Visitor.visitStatement_Exit(self)

class Statement_While(Statement):
  def __init__(self, whilee):
    self.whilee = whilee
  def accept(self, Visitor):
    return Visitor.visitStatement_While(self)

class Statement_Do_While(Statement):
  def __init__(self, dowhilee):
    self.dowhilee = dowhilee
  def accept(self, Visitor):
    return Visitor.visitStatement_Do_While(self)
    
class Statement_Foreach(Statement):
  def __init__(self, foreach):
    self.foreach = foreach
  def accept(self, Visitor):
    return Visitor.visitStatement_Foreach(self)
    
class Statement_Die(Statement):
  def __init__(self, die):
    self.die = die
  def accept(self, Visitor):
    return Visitor.visitStatement_Die(self)
    
class Statement_Global(Statement):
  def __init__(self, _global):
    self._global = _global
  def accept(self, Visitor):
    return Visitor.visitStatement_Global(self)
    
class Statement_For(Statement):
  def __init__(self, _for):
    self._for = _for
  def accept(self, Visitor):
    return Visitor.visitStatement_For(self)

class FuncDecStatement(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ExprParentheses(metaclass = ABCMeta):
  @abstractmethod
  def accept(self,Visitor):
    pass

class ExprParentheses_Expr(ExprParentheses):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExprParentheses_Expr(self)

class funcDecStatement_Function(FuncDecStatement):
  def __init__(self, fds_id, fds_parameter, fds_statements):
    self.fds_id = fds_id
    self.fds_parameter = fds_parameter
    self.fds_statements = fds_statements
  def accept(self, Visitor):
    return Visitor.visitFuncDecStatement_Function(self)

class Fds_id(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Fds_id_withAmpersand(Fds_id):
  def __init__(self, id):
    self.id = id
  def accept(self, Visitor):
    return Visitor.visitFds_id_withAmpersand(self)
    
class Fds_id_noAmpersand(Fds_id):
  def __init__(self, id):
    self.id = id
  def accept(self, Visitor):
    return Visitor.visitFds_id_noAmpersand(self)
    
class Fds_parameter(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Fds_parameter_withParameter(Fds_parameter):
  def __init__(self, parameter_list):
    self.parameter_list = parameter_list
  def accept(self, Visitor):
    return Visitor.visitFds_parameter_withParameter(self)
    
class Fds_parameter_noParameter(Fds_parameter):
  def accept(self, Visitor):
    return Visitor.visitFds_parameter_noParameter()

class Fds_statements(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Fds_statements_withStatements(Fds_statements):
  def __init__(self, inner_statement_MUL):
    self.inner_statement_MUL = inner_statement_MUL
  def accept(self, Visitor):
    return Visitor.visitFds_statements_withStatements(self)
    
class Fds_statements_noStatements(Fds_statements):
  def accept(self, Visitor):
    return Visitor.visitFds_statements_noStatements(self)

class ParameterList(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass
    
class ParameterList_Parameter_Mul(ParameterList):
  def __init__(self, parameter, parameter_list_colon_parameter):
    self.parameter = parameter
    self.parameter_list_colon_parameter = parameter_list_colon_parameter
  def accept(self, Visitor):
    return Visitor.visitParameterList_Parameter_Mul(self)
    
class ParameterList_Parameter_Single(ParameterList):
  def __init__(self, parameter):
    self.parameter = parameter
  def accept(self, Visitor):
    return Visitor.visitParameterList_Parameter_Single(self)
    
class ParameterListColonParameter(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ParameterListColonParameter_Mul(ParameterListColonParameter):
  def __init__(self, parameter, parameterListColonParameter):
    self.parameter = parameter
    self.parameterListColonParameter = parameterListColonParameter
  def accept(self, Visitor):
    return Visitor.visitParameterListColonParameter_Mul(self)

class ParameterListColonParameter_Single(ParameterListColonParameter):
  def __init__(self, parameter):
    self.parameter = parameter
  def accept(self, Visitor):
    return Visitor.visitParameterListColonParameter_Single(self)
    
class Parameter(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass
    
class Parameter_Var(Parameter):
  def __init__(self, variable):
    self.variable = variable
  def accept(self, Visitor):
    return Visitor.visitParameter_Var(self)
    
class Parameter_Prefix_Var(Parameter):
  def __init__(self, prefix, variable):
    self.prefix = prefix
    self.variable = variable
  def accept(self, Visitor):
    return Visitor.visitParameter_Prefix_Var(self)
    
class Parameter_Var_Sufix(Parameter):
  def __init__(self, variable, static_scalar):
    self.variable = variable
    self.static_scalar = static_scalar
  def accept(self, Visitor):
    return Visitor.visitParameter_Var_Sufix(self)
    
class Parameter_Full(Parameter):
  def __init__(self, prefix, variable, static_scalar):
    self.prefix = prefix
    self.variable = variable
    self.static_scalar = static_scalar
  def accept(self, Visitor):
    return Visitor.visitParameter_Full(self)
    
class ParameterPrefix(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ParameterPrefix_PType_Amp(ParameterPrefix):
  def __init__(self, parameter_type):
    self.parameter_type = parameter_type
  def accept(self, Visitor):
    return Visitor.visitParameterPrefix_PType_Amp(self)
    
class ParameterPrefix_Ampersand(ParameterPrefix):
  def accept(self, Visitor):
    return Visitor.visitParameterPrefix_Ampersand(self)
    
class ParameterPrefix_PType(ParameterPrefix):
  def __init__(self, parameter_type):
    self.parameter_type = parameter_type
  def accept(self, Visitor):
    return Visitor.visitParameterPrefix_PType(self)
    
class ParameterType(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ParameterType_Type(ParameterType):
  def __init__(self, p_type):
    self.type = p_type
  def accept(self, Visitor):
    return Visitor.visitParameterType_Type(self)
    
class StaticScalar(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass
    
class StaticScalar_CommonScalar(StaticScalar):
  def __init__(self, common_scalar):
    self.common_scalar = common_scalar
  def accept(self, Visitor):
    return Visitor.visitStaticScalar_CommonScalar(self)
    
class StaticScalar_Plus_Static(StaticScalar):
  def __init__(self, static_scalar):
    self.static_scalar = static_scalar
  def accept(self, Visitor):
    return Visitor.visitStaticScalar_Plus_Static(self)  
  
class StaticScalar_Minus_Static(StaticScalar):
  def __init__(self, static_scalar):
    self.static_scalar = static_scalar
  def accept(self, Visitor):
    return Visitor.visitStaticScalar_Minus_Static(self)  
    
class CommonScalar(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
    
class CommonScalar_Token(CommonScalar):
  def __init__(self, token):
    self.token = token
  def accept(self, Visitor):
    return Visitor.visitCommonScalar_Token(self)
    

class ArrayPairListArrPair(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class ArrayPairList_Mul(ArrayPairListArrPair):
  def __init__(self, arrayPair, arrayPairListArr):
    self.arrayPair = arrayPair
    self.arrayPairListArr = arrayPairListArr
  def accept(self, Visitor):
    return Visitor.visitArrayPairList_Mul(self)

class ArrayPairList_Single(ArrayPairListArrPair):
  def __init__(self,arrayPair):
    self.arrayPair = arrayPair
  def accept(self, Visitor):
    return Visitor.visitArrayPairListArr_Single(self)

class Expr(metaclass = ABCMeta):
  @abstractmethod 
  def accept(self, Visitor):
    pass

class Expr_Plus(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_Plus(self)

class Expr_Plus(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_Plus(self)

class Expr_Minus(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_Minus(self)

class Expr_Uminus(Expr):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExpr_Uminus(self)

class Expr_Times(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_Times(self)

class Expr_Divide(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_Divide(self)

class Expr_Mod(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_Mod(self)

class Expr_Equals(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_Equals(self)

class Expr_NotEquals(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_NotEqual(self)

class Expr_GreatThan(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_GreatThan(self)

class Expr_GreatEqual(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_GreatEqual(self)

class Expr_LessThan(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_LessThan(self)

class Expr_LessEqual(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_LessEqual(self)

class Expr_AndLogical(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_AndLogical(self)

class Expr_OrLogical(Expr):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitExpr_OrLogical(self)
  
class Expr_NotLogical(Expr):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExpr_NotLogical(self)

class Expr_PreIncrement(Expr):
  def __init__(self, variable):
    self.variable =  variable
  def accept(self, Visitor):
    return Visitor.visitExpr_PreIncrement(self)

class Expr_PosIncrement(Expr):
  def __init__(self, variable):
    self.variable =  variable
  def accept(self, Visitor):
    return Visitor.visitExpr_PosIncrement(self)

class Expr_PreDecrement(Expr):
  def __init__(self, variable):
    self.variable =  variable
  def accept(self, Visitor):
    return Visitor.visitExpr_PreDecrement(self)

class Expr_PosDecrement(Expr):
  def __init__(self, variable):
    self.variable =  variable
  def accept(self, Visitor):
    return Visitor.visitExpr_PosDecrement(self)

class Expr_Variable(Expr):
  def __init__(self, variable):
    self.variable =  variable
  def accept(self, Visitor):
    return Visitor.visitExpr_Variable(self)

class Expr_ParenExpr(Expr):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExpr_ParenExpr(self)

class Expr_ArrayDeclaration(Expr):
  def __init__(self, arrayDecl):
    self.arrayDecl = arrayDecl
  def accept(self, Visitor):
    return Visitor.visitExpr_ArrayDeclaration(self)

class Expr_FunctionCall(Expr):
  def __init__(self, functionCall):
    self.functionCall = functionCall
  def accept(self, Visitor):
    return Visitor.visitExpr_FunctionCall(self)

class Expr_Scalar(Expr):
  def __init__(self, scalar):
    self.scalar = scalar
  def accept(self, Visitor):
    return Visitor.visitExpr_Scalar(self)

class Expr_Boolean(Expr):
  def __init__(self, token):
    self.token = token
  def accept(self, Visitor):
    return Visitor.visitExpr_Boolean(self)

class Expr_TernaryOp(Expr):
  def __init__(self, expr1,expr2,expr3):
    self.expr1 = expr1
    self.expr2 = expr2
    self.expr3 = expr3
  def accept(self, Visitor):
    return Visitor.visitExpr_TernaryOp(self)

class Expr_AssignExpr(Expr):
  def __init__(self, variable,expr):
    self.variable = variable
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExpr_AssignExpr(self)

class Expr_AddAssignExpr(Expr):
  def __init__(self, variable,expr):
    self.variable = variable
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExpr_AddAssignExpr(self)

class Expr_SubAssignExpr(Expr):
  def __init__(self, variable,expr):
    self.variable = variable
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExpr_SubAssignExpr(self)

class Expr_ModAssignExpr(Expr):
  def __init__(self, variable,expr):
    self.variable = variable
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExpr_ModAssignExpr(self)

class Expr_DivideAssignExpr(Expr):
  def __init__(self, variable,expr):
    self.variable = variable
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExpr_DivideAssignExpr(self)

class Expr_TimesAssignExpr(Expr):
  def __init__(self, variable,expr):
    self.variable = variable
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExpr_TimesAssignExpr(self)

class Expr_TypeCastOp(Expr):
  def __init__(self, typeCast,expr):
    self.typeCast = typeCast
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExpr_TypeCastOp(self)

class Expr_NumberInt(Expr):
  def __init__(self,numberInt):
    self.numberInt =  numberInt
  def accept(self, Visitor):
    return Visitor.visitExpr_NumberInt(self)

class Expr_NumberFloat(Expr):
  def __init__(self,numberFloat):
    self.numberFloat =  numberFloat
  def accept(self, Visitor):
    return Visitor.visitExpr_NumberFloat(self)

class Expr_EncapsedString(Expr):
  def __init__(self,encapsedString):
    self.encapsedString =  encapsedString
  def accept(self, Visitor):
    return Visitor.visitExpr_EncapsedString(self)

class TypeCastOp(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class TypeCastOp_Token(TypeCastOp):
  def __init__(self, token):
    self.token = token
  def accept(self, Visitor):
    return Visitor.visitTypeCastOp_Token(self)
    
class AssignOperator(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class AssignOperator_Token(AssignOperator):
  def __init__(self, token):
    self.token = token
  def accept(self, Visitor):
    return Visitor.visitAssignOperator_Token(self)

class ArrayDeclaration(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class ArrayDec_WithPairList(ArrayDeclaration):
  def __init__(self, arrayPairList):
    self.arrayPairList = arrayPairList
  def accept(self, Visitor):
    return Visitor.visitArrayDec_WithPairList(self)
    
class ArrayDec_NoPairList(ArrayDeclaration):
  def accept(self, Visitor):
    return Visitor.visitArrayDec_NoPairList(self)

class ArrayPairList(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class ArrayPairList_ArrayPair_Mul(ArrayPairList):
  def __init__(self, arrayPair, arrayPairListArrPair):
    self.arrayPair = arrayPair
    self.arrayPairListArrPair = arrayPairListArrPair
  def accept(self, Visitor):
    return Visitor.visitArrayPairList_ArrayPair_Mul(self)

class ArrayPairList_ArrayPair_Single(ArrayPairList):
  def __init__(self,arrayPair):
    self.arrayPair = arrayPair
  def accept(self, Visitor):
    return Visitor.visitArrayPairList_ArrayPair_Single(self)

class ArrayPair(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ArrayPair_Expr(ArrayPair):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitArrayPair_Expr(self)

class ArrayPair_Variable(ArrayPair):
  def __init__(self, variable):
    self.variable = variable
  def accept(self, Visitor):
    return Visitor.visitArrayPair_Variable(self)

class ArrayPair_Attr_AmpersandVariable(ArrayPair):
  def __init__(self,expr1,expr2):
    self.expr1 =  expr1
    self.expr2 =  expr2
  def accept(self,Visitor):
    return Visitor.visitArrayPair_Attr_AmpersandVariable(self)

class ArrayPair_Attr_Expr(ArrayPair):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1 
    self.expr2 = expr2
  def accept(self, Visitor):
    return Visitor.visitArrayPair_Attr_Expr(self) 
    
class FunctionCall(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class FunctionCall_NoParameter(FunctionCall):
  def __init__(self, id):
    self.id = id
  def accept(self, Visitor):
    return Visitor.visitFunctionCall_NoParameter(self)
    
class FunctionCall_WithParameter(FunctionCall):
  def __init__(self, id, parameterList):
    self.id = id
    self.parameterList = parameterList
  def accept(self, Visitor):
    return Visitor.visitFunctionCall_WithParameter(self)
    
class FCParameterList(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class FCParameterList_Single(FCParameterList):
  def __init__(self, fcParameter):
    self.fcParameter = fcParameter
  def accept(self, Visitor):
    return Visitor.visitFCParameterList_Single(self)

class FCParameterList_Mul(FCParameterList):
  def __init__(self, fcParameter, fcColonParameter):
    self.fcParameter = fcParameter
    self.fcColonParameter = fcColonParameter
  def accept(self, Visitor):
    return Visitor.visitFCParameterList_Mul(self)
    
class FCParameterListColonParameter(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class FCParameterListColonParameter_Single(FCParameterListColonParameter):
  def __init__(self, fcParameter):
    self.fcParameter = fcParameter
  def accept(self, Visitor):
    return Visitor.visitFCParameterListColonParameter_Single(self)
    
class FCParameterListColonParameter_Mul(FCParameterListColonParameter):
  def __init__(self, fcParameter, fcplColonParameter):
    self.fcParameter = fcParameter
    self.fcplColonParameter = fcplColonParameter
  def accept(self, Visitor):
    return Visitor.visitFCParameterListColonParameter_Mul(self)

class FunctionCallParameter(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class FunctionCallParameter_Expr(FunctionCallParameter):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitFunctionCallParameter_Expr(self)
    
class FunctionCallParameter_AmpersandVariable(FunctionCallParameter):
  def __init__(self, variable):
    self.variable = variable
  def accept(self, Visitor):
    return Visitor.visitFunctionCallParameter_AmpersandVariable(self)

class Variable(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Variable_Single(Variable):
  def __init__(self, token):
    self.token = token
  def accept(self, Visitor):
    return Visitor.visitVariable_Single(self)
    
class Variable_Array(Variable):
  def __init__(self, token, selector):
    self.token = token
    self.selector = selector
  def accept(self, Visitor):
    pass

class AmpersandVariable(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class AmpersandVariable_WithAmp(AmpersandVariable):
  def __init__(self, variable_token):
    self.variable_token = variable_token
  def accept(self, Visitor):
    return Visitor.visitAmpersandVariable_WithAmp(self)
    
class AmpersandVariable_NoAmp(AmpersandVariable):
  def __init__(self, variable_token):
    self.variable_token = variable_token
  def accept(self, Visitor):
    return Visitor.visitAmpersandVariable_NoAmp(self)
    
class ForStatement(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
    
class ForStatement_For(ForStatement):
  def __init__(self, forParameters, statementBlock):
    self.forParameters = forParameters
    self.statementBlock = statementBlock
  def accept(self, Visitor):
    return Visitor.visitForStatement_For(self)
    
class ForParameters(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ForParameters_Empty(ForParameters):
  def accept(self, Visitor):
    return Visitor.visitForParameters_Empty()
    
class ForParameters_Left(ForParameters):
  def __init__(self, forExprLeft):
    self.forExprLeft = forExprLeft
  def accept(self, Visitor):
    return Visitor.visitForParameters_Left(self)
    
class ForParameters_Left_Mid(ForParameters):
  def __init__(self, forExprLeft, forExprMid):
    self.forExprLeft = forExprLeft
    self.forExprMid = forExprMid
  def accept(self, Visitor):
    return Visitor.visitForParameters_Left_Mid(self)
    
class ForParameters_Left_Right(ForParameters):
  def __init__(self, forExprLeft, forExprRight):
    self.forExprLeft = forExprLeft
    self.forExprRight = forExprRight
  def accept(self, Visitor):
    return Visitor.visitForParameters_Left_Right(self)
    
class ForParameters_Mid(ForParameters):
  def __init__(self, forExprMid):
    self.forExprMid = forExprMid
  def accept(self, Visitor):
    return Visitor.visitForParameters_Mid(self)
    
class ForParameters_Mid_Right(ForParameters):
  def __init__(self, forExprMid, forExprRight):
    self.forExprMid = forExprMid
    self.forExprRight = forExprRight
  def accept(self, Visitor):
    return Visitor.visitForParameters_Mid_Right(self)
    
class ForParameters_Right(ForParameters):
  def __init__(self, forExprRight):
    self.forExprRight = forExprRight
  def accept(self, Visitor):
    return Visitor.visitForParameters_Right(self)
    
class ForParameters_Full(ForParameters):
  def __init__(self, forExprLeft, forExprMid, forExprRight):
    self.forExprLeft = forExprLeft
    self.forExprMid = forExprMid
    self.forExprRight = forExprRight
  def accept(self, Visitor):
    return Visitor.visitForParameters_Full(self)
    
class ForExprOpt(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ForExprOpt_Single(ForExprOpt):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitForExprOpt_Single(self)
  
class ForExprOpt_Mul(ForExprOpt):
  def __init__(self, expr, forExprOpt):
    self.expr = expr
    self.forExprOpt = forExprOpt
  def accept(self, Visitor):
    return Visitor.visitForExprOpt_Mul(self)
    
class ForExprColonExpr(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ForExprColonExpr_Single(ForExprColonExpr):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitForExprColonExpr_Single(self)
    
class ForExprColonExpr_Mul(ForExprColonExpr):
  def __init__(self, expr, forExprColonExpr):
    self.expr = expr
    self.forExprColonExpr = forExprColonExpr
  def accept(self, Visitor):
    return Visitor.visitForExprColonExpr_Mul(self)

class GlobalStatement(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class GlobalStatement_Single(GlobalStatement):
  def __init__(self, globalVar):
    self.globalVar = globalVar
  def accept(self, Visitor):
    return Visitor.visitGlobalStatement_Single(self)
    
class GlobalStatement_Mul(GlobalStatement):
  def __init__(self, globalVar, colonGlobal):
    self.globalVar = globalVar
    self.colonGlobal = colonGlobal
  def accept(self, Visitor):
    return Visitor.visitGlobalStatement_Mul(self)
    
class GlobalVarMul(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class GlobalVarMul_Single(GlobalVarMul):
  def __init__(self, globalVar):
    self.globalVar = globalVar
  def accept(self, Visitor):
    return Visitor.visitGlobalVarMul_Single(self)
    
class GlobalVarMul_Mul(GlobalVarMul):
  def __init__(self, globalVar, globalVarMul):
    self.globalVar = globalVar
    self.globalVarMul = globalVarMul
  def accept(self, Visitor):
    return Visitor.visitGlobalVarMul_Mul(self)
    
class GlobalVar(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class GlobalVar_Var(GlobalVar):
  def __init__(self, variable):
    self.variable = variable
  def accept(self, Visitor):
    return Visitor.visitGlobalVar_Var(self)
    
class GlobalVar_DolarVar(GlobalVar):
  def __init__(self, variable):
    self.variable = variable
  def accept(self, Visitor):
    return Visitor.visitGlobalVar_DolarVar(self)
    
class GlobalVar_DolarExpr(GlobalVar):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitGlobalVar_DolarExpr(self)
    
class Exit(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class Exit_ExitExpr(Exit):
  def __init__(self, exitExpr):
    self.exitExpr = exitExpr
  def accept(self, Visitor):
    return Visitor.visitExit_ExitExpr(self)
    
class Exit_Empty(Exit):
  def accept(self, Visitor):
    return Visitor.visitExit_Empty()
    
class Die(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Die_ExitExpr(Die):
  def __init__(self, exitExpr):
    self.exitExpr = exitExpr
  def accept(self, Visitor):
    return Visitor.visitDie_ExitExpr(self)
    
class Die_Empty(Die):
  def accept(self, Visitor):
    return Visitor.visitDie_Empty()
    
class ExitExpr(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ExitExpr_Expr(ExitExpr):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitExitExpr_Expr(self)
    
class ExitExpr_Empty(ExitExpr):
  def accept(self, Visitor):
    return Visitor.visitExitExpr_Empty()
    
class Break(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Break_Expr(Break):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitBreak_Expr(self)
    
class Break_Empty(Break):
  def accept(self, Visitor):
    return Visitor.visitBreak_Empty()
    
class Continue(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Continue_Expr(Continue):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitContinue_Expr(self)
    
class Continue_Empty(Continue):
  def accept(self, Visitor):
    return Visitor.visitContinue_Empty()
    
class Return(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Return_Expr(Return):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitReturn_Expr(self)
    
class Return_Empty(Return):
  def accept(self, Visitor):
    return Visitor.visitReturn_Empty()

class Selector(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class SelectorWithExpr(Selector):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    return Visitor.visitSelectorWithExpr(self)

class SelectorWithoutExpr(Selector):
  def accept(self, Visitor):
    return Visitor.visitSelectorWithoutExpr(self)
    
class ForeachStatement(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ForeachStatement_NoAssoc(ForeachStatement):
  def __init__(self, expr, ampVariable, statementBlockOpt):
    self.expr = expr
    self.ampVariable = ampVariable
    self.statementBlockOpt = statementBlockOpt
  def accept(self, Visitor):
    return Visitor.visitForeachStatement_NoAssoc(self)
    
class ForeachStatement_WithAssoc(ForeachStatement):
  def __init__(self, expr, ampVariableKey, ampVariableValue, statementBlockOpt):
    self.expr = expr
    self.ampVariableKey = ampVariableKey
    self.ampVariableValue = ampVariableValue
    self.statementBlockOpt = statementBlockOpt
  def accept(self, Visitor):
    return Visitor.visitForeachStatement_WithAssoc(self)

class WhileStatement(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class WhileStatementSingle(WhileStatement):
  def __init__(self, exprparentheses, statement):
    self.exprparentheses = exprparentheses
    self.statement = statement
  def accept(self, Visitor):
    return Visitor.visitWhileStatementSingle(self)

class StatementBlockOpt_Empty(StatementBlockOpt):
  def accept(self, Visitor):
    return Visitor.visitStatementBlockOpt_Empty(self)

class statementMulMul(StatementMul):
  def __init__(self, statement, statementMul):
    self.statement = statement
    self.statementMul = statementMul
  def accept(self, Visitor):
    return Visitor.visitstatementMulMul(self)
  
class statementMulSingle(StatementMul):
  def __init__(self, statement):
    self.statement = statement
  def accept(self, Visitor):
    return Visitor.visitstatementMulSingle(self)

class DoWhileStatement(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class DoWhileStatementSingle(DoWhileStatement):
  def __init__(self, statementblockopt, exprparentheses):
    self.statementblockopt = statementblockopt
    self.exprparentheses = exprparentheses
  def accept(self, Visitor):
    return Visitor.visitDoWhileStatementSingle(self)
