


class Visitor():
    

    def visitSomaExp(self,somaExp):
        somaExp.exp1.accept(self)
        print('+')
        somaExp.exp2.accept(self)


    def visitMulExp(self,mulExp):
        mulExp.exp1.accept(self)
        print('*')
        mulExp.exp2.accept(self)

    def visitPotExp(self,potExp):
        potExp.exp1.accept(self)
        print("^")
        potExp.exp2.accept(self)

    def visitCallExp(self,callExp):
        callExp.call.accept(self)
    
    def visitAssignExp(self,assignExp):
        assignExp.assign.accept(self)
    
    def visitNumExp(self,numExp):
        print(numExp.num)
        
    def visitIDExp(self,idExp):
        print(idExp.id)
    
    def visitParamsCall(self,paramsCall):
        
        print(paramsCall.id)
        print('(')
        paramsCall.call.accept(self)
        print(')')

    def visitSimpleCall(self,simpleCall):
        print(simpleCall.id)
        print('( )')

    def visitCompoundParams(self,compoundParams):
        print(compoundParams.id)
        print(',')
        compoundParams.params.accept(self)

    def visitSingleParam(self,singleParam):
       print(singleParam.id)

    def visitAssignSimple(self,assignCompound):
        print(assignCompound.id)
        print('=')
        assignCompound.exp.accept(self)