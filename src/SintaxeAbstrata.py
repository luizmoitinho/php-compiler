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
    
class AmpersandVariable(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class GlobalVar(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class ExprParen(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass    

class StatementIf(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass 

class StatementElseIf(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass 

class StatementElse(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass 

class StatementForeach(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass 

class StatementForeachFirst(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass 

class FunctionCall(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class FuncCallParamList(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass  

class FuncCallParam(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass 

class TypeCastOperator(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass 

class ArithmeticOperator(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass 

class AssignOperator(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass 

class ComparissonOperator(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass 

class Expr(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class exprExitExpr(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class Variable(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class BaseVariable(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class ReferenceVariable(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class Selector(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class StaticArrPairList(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class StaticArrayPair(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class ArrayPairList(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class ArrayPair(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass