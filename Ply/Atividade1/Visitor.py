class Visitor():
  def visitSomaExp(self, SomaExp):
    SomaExp.exp1.accept(self)
    print('+', end = ' ')
    SomaExp.exp2.accept(self)
    
  def visitMulExp(self, MulExp):
    MulExp.exp1.accept(self)
    print('*', end = ' ')
    MulExp.exp2.accept(self)
  
  def visitPotExp(self, PotExp):
    PotExp.exp1.accept(self)
    print('^', end = ' ')
    PotExp.exp2.accept(self)
    
  def visitCallExp(self, CallExp):
    CallExp.call.accept(self)
    
  def visitAssignExp(self, AssignExp):
    AssignExp.assign.accept(self)
    
  def visitNumExp(self, NumExp):
    print(NumExp.num, end = ' ')
    
  def visitIDExp(self, IDExp):
    print(IDExp.id, end = ' ')
    
  def visitParamsCall(self, ParamsCall):
    print(ParamsCall.id, end = ' ')
    print('(', end = ' ')
    ParamsCall.call.accept(self)
    print(')', end = ' ')
    
  def visitSimpleCall(self, SimpleCall):
    print(SimpleCall.id, end = ' ')
    print('(', end = ' ')
    print(')', end = ' ')
    
  def visitCompoundParams(self, CompoundParams):
     print(CompoundParams.id, end = ' ')
     print(',', end = ' ')
     CompoundParams.Params.accept(self)
    
  def visitSingleParam(self, SingleParam):
    print(SingleParam.id, end = ' ')
    
  def visitAssignC(self, AssignC):
    print(AssignC.id, end =' ')
    print('=', end = ' ')
    AssignC.Exp.accept(self)
