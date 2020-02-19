from abc import abstractclassmethod
from abc import ABCMeta

class Exp(metaclass=ABCMeta):
  @abstractclassmethod
  def accept(self, Visitor):
    pass

class Call(metaclass=ABCMeta):
  @abstractclassmethod
  def accept(self, Visitor):
    pass

class Assign(metaclass=ABCMeta):
  @abstractclassmethod
  def accept(self, Visitor):
    pass

class Params(metaclass=ABCMeta):
  @abstractclassmethod
  def accept(self, Visitor):
    pass


class SomaExp(Exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, Visitor):
    Visitor.visitSomaExp(self)
    
class MulExp(Exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, Visitor):
    Visitor.visitMulExp(self)
    
class PotExp(Exp):
  def __init__(self, exp1, exp2):
    self.exp1 = exp1
    self.exp2 = exp2

  def accept(self, Visitor):
    Visitor.visitPotExp(self)
    
class CallExp(Exp):
  def __init__(self, call):
    self.call = call

  def accept(self, Visitor):
    Visitor.visitCallExp(self)
    
class AssignExp(Exp):
  def __init__(self, assign):
    self.assign = assign

  def accept(self, Visitor):
    Visitor.visitAssignExp(self)
    
class NumExp(Exp):
  def __init__(self, num):
    self.num = num
  
  def accept(self, Visitor):
    Visitor.visitNumExp(self)
    
class IDExp(Exp):
  def __init__(self, id):
    self.id = id
  
  def accept(self, Visitor):
    Visitor.visitIDExp(self)
    
#-------------------------------------------------------------

class ParamsCall(Call):
  def __init__(self, id, call):
    self.id = id
    self.call = call
    
  def accept(self, Visitor):
    Visitor.visitParamsCall(self)
    
class SimpleCall(Call):
  def __init__(self, id):
    self.id = id
    
  def accept(self, Visitor):
    Visitor.visitSimpleCall(self)
  
#-------------------------------------------------------------
class CompoundParams(Params):
  def __init__(self, id, Params):
    self.id = id
    self.Params = Params
  def accept(self, Visitor):
    Visitor.visitCompoundParams(self)

class SingleParam(Params):
  def __init__(self, id):
    self.id = id
    
  def accept(self, Visitor):
    Visitor.visitSingleParam(self)
#-------------------------------------------------------------  
  
class AssignExp(Assign):
  def __init__(self, id, Exp):
    self.id = id
    self.Exp = Exp
    
  def accept(self, Visitor):
    Visitor.visitAssignExp(self)
