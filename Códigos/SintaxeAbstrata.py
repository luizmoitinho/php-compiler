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
    

#MAIN_INNER ABSTRATA E CONCRETAS  
class MainInner(metaclass=ABCMeta):
  @abstractmethod
  def accept(self, Visitor):
    pass

class MainInner_InnerStatement(MainInner):
  def __init__(self, innerStatement, mainInner):
    self.innerStatement = innerStatement
    self.mainInner = mainInner
  def accept(self, Visitor):
    Visitor.visitMainInner_InnerStatement(self)

#pag 58 pdf ply
class MainInner_Empty(MainInner):
  def __init__(self):
    self.empty = [ ]
  def accept(self, Visitor):
    Visitor.visitMainInner_Empty(self)

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
  def __init__(self,funcDecStatement):
    self.funcDecStatement = funcDecStatement
  def accecpt(self, Visitor):
    Visitor.visitInnerStatement_FuncDecStatement(self)

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
    
class Expr_True(Expr):
  def __init__(self, true):
    self.true = true
  def accept(self, Visitor):
    Visitor.visitExpr_True(self)


class Expr_ArithmeticOperator(Expr):
  def __init__(self, exp1, arithmeticOperator, exp2):
    self.exp1 = exp1
    self.arithmeticOperator = arithmeticOperator
    self.exp2 = exp2
  def accept(self, Visitor):
    Visitor.visitMainInnerStatement(self)




class Encaps(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class EncapsVar(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class encapsVarOPT(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class EncapsVarOffSet(metaclass = ABCMeta):
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

class FuncDecStatement(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class ParameterList(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class Parameter(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class StaticScalar(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
      pass

class CommonScalar(metaclass = ABCMeta):
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



# ========== CLASSES CONCRETAS ================
#class ClasseAbstrata_NomeRegra(NomeClasseAbstrata):
#   .....
#   .....




    




'''


class ArithmeticOp_Soma(ArithmeticOperator):
  def __init__(self, op):
    self.exp1 = op
  def accept(self, Visitor):
    Visitor.visitArithmeticOp_Soma(self)



class FunctionCallExpr(MainInner):
  def __init__(self, exp1):
    self.functionCall = functionCall
  def accept(self, Visitor):
    Visitor.visitMainInnerStatement(self)

class FunctionCallExpr(MainInner):
  def __init__(self, functionCall):
    self.functionCall = functionCall
  def accept(self, Visitor):
    Visitor.visitMainInnerStatement(self)
    






class MainInnerStatement(MainInner):
  def __init__(self, mainInner):
    self.mainInner = mainInner

  def accept(self, Visitor):
    Visitor.visitMainInnerStatement(self)
    
class NumberRealCommonScalar(CommonScalar):
  def __init__(self,numberReal):
    self.numberReal = numberReal
  def accept(self,Visitor):
    Visitor.visitNumberRealCommonScalar(self)

class NumberIntegerCommonScalar(CommonScalar):
    def __init__(self,numberReal):
        self.numberInteger = numberInteger
    def accept(self,Visitor):
        Visitor.visitNumberIntegerCommonScalar(self)        

class ConstantEncapStrCommonScalar(CommonScalar):
    def __init__(self,numberReal):
        self.ConstantEncapStr = ConstantEncapStr
    def accept(self,Visitor):
        Visitor.visitConstantEncapStrCommonScalar(self)        

class PlusStaticScalar(CommonScalar):
    def __init__(self,numberReal):
        self.ConstantEncapStr = ConstantEncapStr
    def accept(self,Visitor):
        Visitor.visitConstantEncapStrCommonScalar(self)       

'''