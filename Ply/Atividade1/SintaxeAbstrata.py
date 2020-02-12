from abc import abstractclassmethod
from abc import ABCMeta

class Exp(metaclass=ABCMeta):
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
    
class CallExp(Call):
  def __init__(self, call):
    self.call = call

  def accept(self, Visitor):
    Visitor.visitCallExp(self)
    
class AssignExp(Assign):
  def __init__(self, assign):
    self.assign = assign

  def accept(self, Visitor):
    Visitor.visitAssignExp(self)
    
class NumExp(num):
  def __init__(self, num):
    self.num = num
  
  def accept(self, Visitor):
    Visitor.visitNumExp(self)
    
class IDExp(id):
  def __init__(self, id):
    self.id = id
  
  def accept(self, Visitor):
    Visitor.visitIDExp(self)
    
#-------------------------------------------------------------

class Call(metaclass=ABCMeta):
  @abstractclassmethod
  def accept(self, Visitor):
    pass

class ParamsCall(Call):
  def __init__(self, id, Params):
    self.id = id
    self.Params = Params
    
  def accept(self, Visitor):
    Visitor.visitParamsCall(self)
    
class SimpleCall(Call):
  def __init__(self, id):
    self.id = id
    
  def accept(self, Visitor):
    Visitor.visitSimpleCall(self)
  
#-------------------------------------------------------------

class Params(metaclass=ABCMeta):
  @abstractclassmethod
  def accept(self, Visitor):
    pass
  
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
  
class Assign(metaclass=ABCMeta):
  @abstractclassmethod
  def accept(self, Visitor):
    pass
  
class AssignExp(Assign):
  def __init__(self, id, Exp):
    self.id = id
    self.Exp = Exp
    
  def accept(self, Visitor):
    Visitor.visitAssignExp(self)
