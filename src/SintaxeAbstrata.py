from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

# ========== CLASSES ABSTRATAS ================

class Main(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Main_MainInner(Main):
  def __init__(self, mainInner):
    self.mainInner = mainInner
  def accept(self, Visitor):
    Visitor.visitMain_MainInner(self)
    
class Main_MainInner_Empty(Main):
  def accept(self, Visitor):
    Visitor.visitMain_MainInner_Empty(self)
    

#MAIN_INNER ABSTRATA E CONCRETAS  
class MainInner(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class MainInner_InnerStatement_MainInner(MainInner):
  def __init__(self, innerStatement, mainInner):
    self.innerStatement = innerStatement
    self.mainInner = mainInner
  def accept(self, Visitor):
    Visitor.visitMainInner_InnerStatement_MainInner(self)

class MainInner_InnerStatement(MainInner):
  def __init__(self, innerStatement):
    self.innerStatement = innerStatement
  def accept(self, Visitor):
    Visitor.visitMainInner_InnerStatement(self)

class InnerStatement(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass
    
class InnerStatement_Statement(InnerStatement):
  def __init__(self, statement):
    self.statement = statement
  def accept(self, Visitor):
    Visitor.visitInnerStatement_Statement(self)
    
class InnerStatement_FuncDecStatement(InnerStatement):
  def __init__(self, funcDecStatement):
    self.funcDecStatement = funcDecStatement
  def accept(self, Visitor):
    Visitor.visitInnerStatement_FuncDecStatement(self)
    
class InnerStatementMul(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class InnerStatementMul_Mul(InnerStatementMul):
  def __init__(self, innerStatement, innerStatementMul):
    self.innerStatement = innerStatement
    self.innerStatementMul = innerStatementMul
  def accept(self, Visitor):
    Visitor.visitInnerStatementMul_Mul(self)
    
class InnerStatementMul_Single(InnerStatementMul):
  def __init__(self, innerStatement):
    self.innerStatement = innerStatement
  def accept(self, Visitor):
    Visitor.visitInnerStatementMul_Single(self)

class Statement(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass
    
class Statement_Expr(Statement):
  def __init__(self, expr, semiColon):
    self.expr = expr
    self.semiColon = semiColon
  def accept(self, Visitor):
    Visitor.visitStatement_Expr(self)
    
class Statement_Break(Statement):
  def __init__(self, _break):
    self._break = _break
  def accept(self, Visitor):
    Visitor.visitStatement_Break(self)
    
class Statement_Continue(Statement):
  def __init__(self, _continue):
    self._continue = _continue
  def accept(self, Visitor):
    Visitor.visitStatement_Continue(self)
    
class Statement_Return(Statement):
  def __init__(self, _return):
    self._return = _return
  def accept(self, Visitor):
    Visitor.visitStatement_Return(self)
  
class Statement_Exit(Statement):
  def __init__(self, exit):
    self.exit = exit
  def accept(self, Visitor):
    Visitor.visitStatement_Exit(self)
    
class Statement_Die(Statement):
  def __init__(self, die):
    self.die = die
  def accept(self, Visitor):
    Visitor.visitStatement_Die(self)

class FuncDecStatement(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class funcDecStatement_Function(FuncDecStatement):
  def __init__(self, fds_id, fds_parameter, fds_statements):
    self.fds_id = fds_id
    self.fds_parameter = fds_parameter
    self.fds_statements = fds_statements
  def accept(self, Visitor):
    Visitor.visitFuncDecStatement_Function(self)

class Fds_id(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Fds_id_withAmpersand(Fds_id):
  def __init__(self, id):
    self.id = id
  def accept(self, Visitor):
    Visitor.visitFds_id_withAmpersand(self)
    
class Fds_id_noAmpersand(Fds_id):
  def __init__(self, id):
    self.id = id
  def accept(self, Visitor):
    Visitor.visitFds_id_noAmpersand(self)
    
class Fds_parameter(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Fds_parameter_withParameter(Fds_parameter):
  def __init__(self, parameter_list):
    self.parameter_list = parameter_list
  def accept(self, Visitor):
    Visitor.visitFds_parameter_withParameter(self)
    
class Fds_parameter_noParameter(Fds_parameter):
  def accept(self, Visitor):
    Visitor.visitFds_parameter_noParameter(self)

class Fds_statements(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Fds_statements_withStatements(Fds_statements):
  def __init__(self, inner_statement_MUL):
    self.inner_statement_MUL = inner_statement_MUL
  def accept(self, Visitor):
    Visitor.visitFds_statements_withStatements(self)
    
class Fds_statements_noStatements(Fds_statements):
  def accept(self, Visitor):
    Visitor.visitFds_statements_noStatements(self)

class ParameterList(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass
    
class ParameterList_Parameter_Mul(ParameterList):
  def __init__(self, parameter, parameter_list_colon_parameter):
    self.parameter = parameter
    self.parameter_list_colon_parameter = parameter_list_colon_parameter
  def accept(self, Visitor):
    Visitor.visitParameterList_Parameter_Mul(self)
    
class ParameterList_Parameter_Single(ParameterList):
  def __init__(self, parameter):
    self.parameter = parameter
  def accept(self, Visitor):
    Visitor.visitParameterList_Parameter_Single(self)
    
class ParameterListColonParameter(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ParameterListColonParameter_Mul(ParameterListColonParameter):
  def __init__(self, parameter, parameterListColonParameter):
    self.parameter = parameter
    self.parameterListColonParameter = parameterListColonParameter
  def accept(self, Visitor):
    Visitor.visitParameterListColonParameter_Mul(self)

class ParameterListColonParameter_Single(ParameterListColonParameter):
  def __init__(self, parameter):
    self.parameter = parameter
  def accept(self, Visitor):
    Visitor.visitParameterListColonParameter_Single(self)
    
class Parameter(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass
    
class Parameter_Var(Parameter):
  def __init__(self, variable):
    self.variable = variable
  def accept(self, Visitor):
    Visitor.visitParameter_Var(self)
    
class Parameter_Prefix_Var(Parameter):
  def __init__(self, prefix, variable):
    self.prefix = prefix
    self.variable = variable
  def accept(self, Visitor):
    Visitor.visitParameter_Prefix_Var(self)
    
class Parameter_Var_Sufix(Parameter):
  def __init__(self, variable, static_scalar):
    self.variable = variable
    self.static_scalar = static_scalar
  def accept(self, Visitor):
    Visitor.visitParameter_Var_Sufix(self)
    
class Parameter_Full(Parameter):
  def __init__(self, prefix, variable, static_scalar):
    self.prefix = prefix
    self.variable = variable
    self.static_scalar = static_scalar
  def accept(self, Visitor):
    Visitor.visitParameter_Full(self)
    
class ParameterPrefix(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ParameterPrefix_PType_Amp(ParameterPrefix):
  def __init__(self, parameter_type):
    self.parameter_type = parameter_type
  def accept(self, Visitor):
    Visitor.visitParameterPrefix_PType_Amp(self)
    
class ParameterPrefix_Ampersand(ParameterPrefix):
  def accept(self, Visitor):
    Visitor.visitParameterPrefix_Ampersand(self)
    
class ParameterPrefix_PType(ParameterPrefix):
  def __init__(self, parameter_type):
    self.parameter_type = parameter_type
  def accept(self, Visitor):
    Visitor.visitParameterPrefix_PType(self)
    
class ParameterType(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ParameterType_Type(ParameterType):
  def __init__(self, p_type):
    self.type = p_type
  def accept(self, Visitor):
    Visitor.visitParameterType_Type(self)
    
class StaticScalar(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass
    
class StaticScalar_CommonScalar(StaticScalar):
  def __init__(self, common_scalar):
    self.common_scalar = common_scalar
  def accept(self, Visitor):
    Visitor.visitStaticScalar_CommonScalar(self)
    
class StaticScalar_Plus_Static(StaticScalar):
  def __init__(self, static_scalar):
    self.static_scalar = static_scalar
  def accept(self, Visitor):
    Visitor.visitStaticScalar_Plus_Static(self)  
  
class StaticScalar_Minus_Static(StaticScalar):
  def __init__(self, static_scalar):
    self.static_scalar = static_scalar
  def accept(self, Visitor):
    Visitor.visitStaticScalar_Minus_Static(self)  
    
class CommonScalar(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
    
class CommonScalar_Token(CommonScalar):
  def __init__(self, token):
    self.token = token
  def accept(self, Visitor):
    Visitor.visitCommonScalar_Token(self)
    

class ArrayPairListArrPair(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class ArrayPairList_Mul(ArrayPairListArrPair):
  def __init__(self, arrayPair, arrayPairListArr):
    self.arrayPair = arrayPair
    self.arrayPairListArr = arrayPairListArr
  def accept(self, Visitor):
    Visitor.visitArrayPairList_Mul(self)

class ArrayPairList_Single(ArrayPairListArrPair):
  def __init__(self,arrayPair):
    self.arrayPair = arrayPair
  def accept(self, Visitor):
    Visitor.visitArrayPairListArr_Single(self)


class Expr(metaclass = ABCMeta):
  @abstractmethod 
  def accept(self, Visitor):
    pass

class Expr_Expr1_Expr2(Expr):
  def __init__(self, expr1, expr2):
    self.expr1 = expr1
    self.expr2 = expr2
  def accept(self, Visitor):
    Visitor.visitExpr_Expr1_Expr2(self)
    
class Expr_Expr1(Expr):
  def __init__(self, expr1):
    self.expr1 = expr1
  def accept(self, Visitor):
    Visitor.visitExpr_Expr1(self)
    
class Expr_Expr3(Expr):
  def __init__(self, expr3):
    self.expr3 = expr3
  def accept(self, Visitor):
    Visitor.visitExpr_Expr3(self)
    
class Expr3(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Expr3_TypeCast(Expr3):
  def __init__(self, typeCast, expr):
    self.typeCast = typeCast
    self.expr = expr
  def accept(self, Visitor):
    Visitor.visitExpr3_TypeCast(self)
    
class TypeCastOp(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class TypeCastOp_Token(TypeCastOp):
  def __init__(self, token):
    self.token = token
  def accept(self, Visitor):
    Visitor.visitTypeCastOp_Token(self)

class ArrayDeclaration(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class ArrayDec_WithPairList(ArrayDeclaration):
  def __init__(self, arrayPairList):
    self.arrayPairList = arrayPairList
  def accept(self, Visitor):
    Visitor.visitArrayDec_WithPairList(self)
    
class ArrayDec_NoPairList(ArrayDeclaration):
  def accept(self, Visitor):
    Visitor.visitArrayDec_NoPairList(self)

class ArrayPairList(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class ArrayPairList_ArrayPair_Mul(ArrayPairList):
  def __init__(self, arrayPair, arrayPairListArrPair):
    self.arrayPair = arrayPair
    self.arrayPairListArrPair = arrayPairListArrPair
  def accept(self, Visitor):
    Visitor.visitArrayPairList_ArrayPair_Mul(self)

class ArrayPairList_ArrayPair_Single(ArrayPairList):
  def __init__(self,arrayPair):
    self.arrayPair = arrayPair
  def accept(self, Visitor):
    Visitor.visitArrayPairList_ArrayPair_Single(self)
  
class ArrayPair(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ArrayPair_Expr(ArrayPair):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    Visitor.visitArrayPair_Expr(self)

class ArrayPair_Variable(ArrayPair):
  def __init__(self, variable):
    self.variable = variable
  def accept(self, Visitor):
    Visitor.visitArrayPair_Variable(self)

class ArrayPair_Attr_Expr(ArrayPair):
  def __init__(self, expr1,expr2):
    self.expr1 = expr1 
    self.expr2 = expr2
  def accept(self, Visitor):
    Visitor.visitArrayPair_Attr_Expr(self) 
    
class Expr1(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
    
class Expr1_ExprPar(Expr1):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    Visitor.visitExpr1_ExprPar(self)

class Expr1_FunctionCall(Expr1):
  def __init__(self, functionCall):
    self.functionCall = functionCall
  def accept(self, Visitor):
    Visitor.visitExpr1_FunctionCall(self)

class Expr1_ArrayDeclaration(Expr1):
  def __init__(self, arrayDeclaration):
    self.arrayDeclaration = arrayDeclaration
  def accept(self, Visitor):
    Visitor.visitExpr1_ArrayDeclaration(self)

class Expr1_Scalar(Expr1):
  def __init__(self, scalar):
    self.scalar = scalar
  def accept(self, Visitor):
    Visitor.visitExpr1_Scalar(self)
  
class Expr1_True(Expr1):
  def accept(self, Visitor):
    Visitor.visitExpr1_True(self)
    
class Expr1_False(Expr1):
  def accept(self, Visitor):
    Visitor.visitExpr1_False(self)
  
class Scalar(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Scalar_Token(Scalar):
  def __init__(self, token):
    self.token = token
  def accept(self, Visitor):
    Visitor.visitScalar_Token(self)
    
class FunctionCall(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class FunctionCall_NoParameter(FunctionCall):
  def __init__(self, id):
    self.id = id
  def accept(self, Visitor):
    Visitor.visitFunctionCall_NoParameter(self)
    
class FunctionCall_WithParameter(FunctionCall):
  def __init__(self, id, parameterList):
    self.id = id
    self.parameterList = parameterList
  def accept(self, Visitor):
    Visitor.visitFunctionCall_WithParameter(self)
    
class FCParameterList(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class FCParameterList_Single(FCParameterList):
  def __init__(self, fcParameter):
    self.fcParameter = fcParameter
  def accept(self, Visitor):
    Visitor.visitFCParameterList_Single(self)

class FCParameterList_Mul(FCParameterList):
  def __init__(self, fcParameter, fcColonParameter):
    self.fcParameter = fcParameter
    self.fcColonParameter = fcColonParameter
  def accept(self, Visitor):
    Visitor.visitFCParameterList_Mul(self)
    
class FCParameterListColonParameter(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class FCParameterListColonParameter_Single(FCParameterListColonParameter):
  def __init__(self, fcParameter):
    self.fcParameter = fcParameter
  def accept(self, Visitor):
    Visitor.visitFCParameterListColonParameter_Single(self)
    
class FCParameterListColonParameter_Mul(FCParameterListColonParameter):
  def __init__(self, fcParameter, fcplColonParameter):
    self.fcParameter = fcParameter
    self.fcplColonParameter = fcplColonParameter
  def accept(self, Visitor):
    Visitor.visitFCParameterListColonParameter_Mul(self)

class FunctionCallParameter(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class FunctionCallParameter_Expr(FunctionCallParameter):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    Visitor.visitFunctionCallParameter_Expr(self)
    
class FunctionCallParameter_AmpersandVariable(FunctionCallParameter):
  def __init__(self, variable):
    self.variable = variable
  def accept(self, Visitor):
    Visitor.visitFunctionCallParameter_AmpersandVariable(self)

class Variable(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Variable_Reference_Variable(Variable):
  def __init__(self, reference_variable):
    self.reference_variable = reference_variable
  def accept(self, Visitor):
    Visitor.visitVariable_Reference_Variable(self)
    
class Variable_Simple_Indirect(Variable):
  def __init__(self, simple_indirect, reference_variable):
    self.simple_indirect = simple_indirect
    self.reference_variable = reference_variable
  def accept(self, Visitor):
    Visitor.visitVariable_Simple_Indirect(self)

class ReferenceVariable(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class ReferenceVariable_Compound_Reference(ReferenceVariable):
  def __init__(self, compoundvariable, referencevariableSELECTOR):
    self.compoundvariable = compoundvariable
    self.referencevariableSELECTOR = referencevariableSELECTOR
  def accept(self, Visitor):
    Visitor.visitReferenceVariable_Compound_Reference(self)
    
class ReferenceVariable_Compound(ReferenceVariable):
  def __init__(self, compoundvariable):
    self.compoundvariable = compoundvariable
  def accept(self, Visitor):
    Visitor.visitReferenceVariable_Compound(self)

class SimpleIndirectReference(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class SimpleIndirectReference_Mul(SimpleIndirectReference):
  def __init__(self, simpleindirect):
    self.simpleindirect = simpleindirect
  def accept(self, Visitor):
    Visitor.visitSimpleIndirectReference_Mul(self)

class SimpleIndirectReference_Single(SimpleIndirectReference):
  def accept(self, Visitor):
    Visitor.visitSimpleIndirectReference_Single(self)
    
class Exit(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class Exit_ExitExpr(Exit):
  def __init__(self, exitExpr):
    self.exitExpr = exitExpr
  def accept(self, Visitor):
    Visitor.visitExit_ExitExpr(self)
    
class Exit_Empty(Exit):
  def accept(self, Visitor):
    Visitor.visitExit_Empty()
    
class Die(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Die_ExitExpr(Die):
  def __init__(self, exitExpr):
    self.exitExpr = exitExpr
  def accept(self, Visitor):
    Visitor.visitDie_ExitExpr(self)
    
class Die_Empty(Die):
  def accept(self, Visitor):
    Visitor.visitDie_Empty()
    
class ExitExpr(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class ExitExpr_Expr(ExitExpr):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    Visitor.visitExitExpr_Expr(self)
    
class ExitExpr_Empty(ExitExpr):
  def accept(self, Visitor):
    Visitor.visitExitExpr_Empty()
    
class Break(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Break_Expr(Break):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    Visitor.visitBreak_Expr(self)
    
class Break_Empty(Break):
  def accept(self, Visitor):
    Visitor.visitBreak_Empty()
    
class Continue(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Continue_Expr(Continue):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    Visitor.visitContinue_Expr(self)
    
class Continue_Empty(Continue):
  def accept(self, Visitor):
    Visitor.visitContinue_Empty()
    
class Return(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass
  
class Return_Expr(Return):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    Visitor.visitReturn_Expr(self)
    
class Return_Empty(Return):
  def accept(self, Visitor):
    Visitor.visitReturn_Empty()

class CompoundVariable(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class CompoundVariableSingle(CompoundVariable):
  def __init__(self, variable):
    self.variable = variable
  def accept(self, Visitor):
    Visitor.visitCompoundVariableSingle(self)

class CompoundVariableMul(CompoundVariable):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    Visitor.visitCompoundVariableMul(self)

class ReferenceVariableSelector(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class ReferenceVariableSelectorSingle(ReferenceVariableSelector):
  def __init__(self, selector):
    self.selector = selector
  def accept(self, Visitor):
    Visitor.visitReferenceVariableSelectorSingle(self)

class ReferenceVariableSelectorMul(ReferenceVariableSelector):
  def __init__(self, selector, referencevariableselector):
    self.selector = selector
    self.selector = referencevariableselector
  def accept(self, Visitor):
    Visitor.visitReferenceVariableSelectorMul(self)

class Selector(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class SelectorWithExpr(Selector):
  def __init__(self, expr):
    self.expr = expr
  def accept(self, Visitor):
    Visitor.visitSelectorWithExpr(self)

class SelectorWithoutExpr(Selector):
  def accept(self, Visitor):
    Visitor.visitSelectorWithoutExpr(self)